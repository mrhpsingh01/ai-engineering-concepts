import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()


MODEL = os.environ.get("LLM_MODEL", "gemini-3.8-flash")

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": os.environ["GEMINI_API_KEY"],
}

body = json.dumps({
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": "What is a neural network in one sentence?"}
            ]
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 256
    }
}).encode("utf-8")

req = urllib.request.Request(
    url,
    data=body,
    headers=headers,
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(result["candidates"][0]["content"]["parts"][0]["text"])