import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

MODEL = os.environ.get("LLM_MODEL", "gemini-3.8-flash")

response = client.models.generate_content(
    model=MODEL,
    contents="What is a neural network in one sentence?",
    config={
        "max_output_tokens": 256,
    },
)

print(response.text)