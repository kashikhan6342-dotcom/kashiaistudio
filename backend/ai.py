import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-dev"


def generate_image(prompt, output_path):

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt},
        timeout=120
    )

    if response.status_code != 200:
        return False, response.text

    with open(output_path, "wb") as f:
        f.write(response.content)

    return True, output_path