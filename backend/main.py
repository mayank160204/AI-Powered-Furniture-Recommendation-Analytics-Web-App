from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from recommender import get_recommendations
from analytics import get_analytics
from genai import describe_product
from settings import settings
import json, os, time

app = FastAPI(title="Furniture Recommender")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Query(BaseModel):
    query: str
    brand: str|None=None
    material: str|None=None
    sort_by:str|None=None

class Feedback(BaseModel):
    item_id:str
    liked:bool
    reason:str|None=None

@app.get("/health")
def health():
    return {"status":"ok","text_index":settings.PINECONE_INDEX_TEXT}

@app.post("/recommend")
def recommend(q: Query):
    try:
        items = get_recommendations(q)
        for it in items:
            it["gen_desc"] = describe_product(it)
        return items
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/analytics")
def analytics():
    return get_analytics()

@app.post("/feedback")
def feedback(fb: Feedback):
    os.makedirs("data", exist_ok=True)
    with open("data/feedback.jsonl","a") as f:
        f.write(json.dumps({"ts":time.time(), **fb.model_dump()})+"\n")
    return {"ok":True}
