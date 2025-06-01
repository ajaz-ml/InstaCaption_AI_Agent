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
        output = response.json()
        if "error" in output:
           return f"⚠️ Hugging Face Error: {output['error']}"


        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"]
        else:
            return f"⚠️ Couldn't generate a caption. Raw response: {output}"


    except Exception as e:
        return f"⚠️ Error: {str(e)}"
