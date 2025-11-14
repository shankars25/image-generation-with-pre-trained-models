# dalle_mini_generation.py
# Image Generation using Pretrained DALL-E Mini (Craiyon)

import requests
from PIL import Image
from io import BytesIO
import time

def generate_image(prompt):
    print("Sending request to DALL-E Mini (Craiyon)...")

    url = "https://api.craiyon.com/v3/draw"
    payload = {"prompt": prompt}

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Error: Unable to generate image.")

    data = response.json()
    print("Images generated! Saving...")

    for idx, img_data in enumerate(data["images"]):
        image_bytes = BytesIO(bytes(img_data))
        img = Image.open(image_bytes)
        img.save(f"dalle_mini_output_{idx+1}.png")

    print("Saved all images!")


if __name__ == "__main__":
    text = input("Enter prompt for DALL-E Mini: ")
    generate_image(text)
