import httpx
from app.config import API_KEY, CHAT_MODEL


class LLMClient:
    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def generate(self, context: str, question: str) -> str:
        payload = {
            "model": CHAT_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Answer using only provided context. Do not guess."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {question}"
                }
            ],
            "max_tokens": 300
        }

        response = httpx.post(self.url, headers=self.headers, json=payload, timeout=60)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]