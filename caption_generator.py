import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-common_gen"

HF_TOKEN = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_caption(topic, style, language):
    prompt = f"short caption about {topic} in {language} with {style.lower()} tone"

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        output = response.json()

        # Get the generated text
        if isinstance(output, list):
            text = output[0].get("generated_text", "")
        else:
            text = output.get("generated_text", "")

        # Extract first clean line
        lines = [line.strip("•- ").strip() for line in text.split("\n") if line.strip()]
        best_caption = lines[0] if lines else "⚠️ No caption found."

        # Return all short captions as a list (for multi-option display)
        captions = [line for line in lines if 0 < len(line) < 120]
        return captions

    except Exception as e:
        return f"⚠️ Error: {str(e)}"