from sentence_transformers import SentenceTransformer, CrossEncoder
from pinecone import Pinecone
import numpy as np
from settings import settings

_text_model = SentenceTransformer(settings.MODEL_TEXT_EMB)
_reranker = CrossEncoder(settings.MODEL_RERANK)

pc = Pinecone(api_key=settings.PINECONE_API_KEY)
_index = pc.Index(settings.PINECONE_INDEX_TEXT)

def _price_affinity(user_query_price, item_price):
    if user_query_price is None or item_price is None: return 0.0
    # closer → higher
    return float(np.exp(-abs(user_query_price-item_price)/max(10.0, user_query_price)))

def get_recommendations(q):
    vec = _text_model.encode(q.query).tolist()
    flt = {}
    if q.brand: flt["brand"] = {"$eq": q.brand}
    if q.material: flt["material"] = {"$eq": q.material}
    res = _index.query(vector=vec, top_k=20, include_metadata=True, filter=flt or None)

    matches = res["matches"]
    pairs = [(q.query, m["metadata"]["text"]) for m in matches]
    rerank = _reranker.predict(pairs)

    out = []
    for m, rr in zip(matches, rerank):
        md = m["metadata"]
        s = 0.55*m["score"] + 0.25*float(rr) + 0.10*_price_affinity(None, md.get("price_float")) + 0.10*(1.0 if q.brand and md.get("brand")==q.brand else 0.0)
        out.append({
            "id": m["id"],
            "title": md.get("title"),
            "image": md.get("image"),
            "price": md.get("price"),
            "material": md.get("material"),
            "brand": md.get("brand"),
            "score": float(s)
        })
    out.sort(key=lambda x: x["score"], reverse=True)
    if q.sort_by=="price": out.sort(key=lambda x: float(x["price"] or 0.0))
    return out[:5]
