import pickle
import numpy as np


class VectorStore:
    def __init__(self, emb_dim: int):
        self.emb_dim = emb_dim
        self.embeddings = []
        self.texts = []

    def add(self, embedding: np.ndarray, text: str):
        self.embeddings.append(embedding)
        self.texts.append(text)

    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump({
                "embeddings": self.embeddings,
                "texts": self.texts
            }, f)

    def load(self, path: str):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self.embeddings = data["embeddings"]
            self.texts = data["texts"]

    def get_matrix(self):
        return np.vstack(self.embeddings)