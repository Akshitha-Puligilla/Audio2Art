import requests
import os
from dotenv import load_dotenv

load_dotenv()
SD_API_KEY = os.getenv("STABLE_DIFFUSION_API_KEY")

def generate_image_with_sd(prompt):
    url = "https://stablediffusionapi.com/api/v3/text2img"
    data = {
        "key": SD_API_KEY,
        "prompt": prompt,
        "width": 512,
        "height": 512,
        "samples": 1,
        "num_inference_steps": 30
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["output"][0]  # Adjust based on API's response format
    else:
        raise Exception(f"Error generating image: {response.json()}")
