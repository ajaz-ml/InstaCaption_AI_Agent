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
        output = response.json()

        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"]
        else:
            return "⚠️ Couldn't generate a caption. Try again."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
