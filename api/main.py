from fastapi import FastAPI
from app.rag_engine import RAGEngine

app = FastAPI()
engine = RAGEngine("artifacts/vector_store.pkl")


@app.post("/query")
def query(question: str):
    answer = engine.answer(question)
    return {"answer": answer}