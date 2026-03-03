import httpx
import numpy as np
from app.config import API_KEY, EMBED_MODEL


class Embedder:
    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/embeddings"
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def embed(self, text: str) -> np.ndarray:
        payload = {
            "model": EMBED_MODEL,
            "input": text
        }

        response = httpx.post(self.url, headers=self.headers, json=payload, timeout=60)
        response.raise_for_status()

        return np.array(response.json()["data"][0]["embedding"], dtype=np.float32)