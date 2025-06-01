import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-common_gen"
HF_TOKEN = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_caption(topic, style, language):
    prompt = f"Generate a short, catchy Instagram caption about {topic} in {language} with a {style.lower()} tone"

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        
        # Logging
        print("📡 Status Code:", response.status_code)
        print("📡 Raw Response:", response.text)

        if not response.text.strip():
            return "⚠️ Hugging Face API returned an empty response. Try again later."

        output = response.json()

        # Handle error response
        if isinstance(output, dict) and "error" in output:
            return f"⚠️ Hugging Face Error: {output['error']}"

        # Handle generated output
        if isinstance(output, list) and "generated_text" in output[0]:
            text = output[0]["generated_text"]
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            return lines[0] if lines else "⚠️ No caption found."

        return f"⚠️ Couldn't generate a caption. Raw response: {output}"

    except Exception as e:
        return f"⚠️ Error: {str(e)}"