import os
import requests
from dotenv import load_dotenv
load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

response = requests.post(API_URL, headers=headers, json={"inputs": "Say hi!"})
print(response.status_code)
print(response.json())
