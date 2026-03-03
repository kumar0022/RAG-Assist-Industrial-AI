from app.embedder import Embedder
from app.retrieval import retrieve_top_k
from app.llm_client import LLMClient
from app.vector_store import VectorStore


class RAGEngine:
    def __init__(self, vector_store_path: str):
        self.embedder = Embedder()
        self.llm = LLMClient()
        self.store = VectorStore(emb_dim=1536)
        self.store.load(vector_store_path)

    def answer(self, question: str, top_k=5) -> str:
        query_emb = self.embedder.embed(question)
        emb_matrix = self.store.get_matrix()

        context_chunks = retrieve_top_k(
            query_emb,
            emb_matrix,
            self.store.texts,
            k=top_k
        )

        context = "\n\n".join(context_chunks)
        return self.llm.generate(context, question)