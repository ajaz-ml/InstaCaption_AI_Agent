import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

HF_TOKEN = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_caption(topic, style, language):
    prompt = f"""Generate a short, catchy Instagram caption in {language} for a photo about "{topic}".
It should be {style.lower()}. Keep it under 20 words. Avoid hashtags."""

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        output = response.json()

        # Extract generated text
        if isinstance(output, list):
            text = output[0].get("generated_text", "")
        else:
            text = output.get("generated_text", "")

        # Pick the first non-empty line
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        best_caption = lines[0] if lines else "⚠️ No caption found."

        return best_caption

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
