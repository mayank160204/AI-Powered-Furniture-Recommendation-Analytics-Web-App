from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PINECONE_API_KEY: str
    PINECONE_ENV: str = "us-east-1"
    PINECONE_INDEX_TEXT: str = "furniture-text"
    PINECONE_INDEX_IMAGE: str = "furniture-image"
    GOOGLE_API_KEY: str
    MODEL_TEXT_EMB: str = "all-MiniLM-L6-v2"
    MODEL_RERANK: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()