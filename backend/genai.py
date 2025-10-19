from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from functools import lru_cache
from settings import settings

_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=settings.GOOGLE_API_KEY)
_prompt = PromptTemplate.from_template(
    "Write two short, factual marketing sentences (<=50 words) for: "
    "title='{title}', material='{material}', category='{category}'. "
    "Avoid specs not provided. Tone: warm, trustworthy."
)
_chain = _prompt | _llm

@lru_cache(maxsize=4096)
def describe_product_key(title, material, category):  # cache key
    return _chain.invoke({"title": title or "", "material": material or "", "category": category or ""})

def describe_product(md: dict) -> str:
    return describe_product_key(md.get("title",""), md.get("material",""), md.get("cv_label",""))
