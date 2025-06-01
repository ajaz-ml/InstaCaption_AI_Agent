import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
HF_TOKEN = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_caption(topic, style, language):
    prompt = f"""Generate a short, catchy Instagram caption in {language} for a photo about "{topic}".
It should be {style.lower()}. Keep it under 20 words. Avoid hashtags."""

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        # 💡 Handle empty response cleanly
        if not response.text.strip():
            return "⚠️ Hugging Face API returned an empty response. Please try again in a moment."

        output = response.json()

        # Get raw text
        if isinstance(output, list):
            text = output[0].get("generated_text", "")
        else:
            text = output.get("generated_text", "")

        # Split into clean lines
        lines = [line.strip("•- ").strip() for line in text.split("\n") if line.strip()]
        captions = [line for line in lines if 0 < len(line) < 120]

        return captions if captions else "⚠️ No caption found."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
