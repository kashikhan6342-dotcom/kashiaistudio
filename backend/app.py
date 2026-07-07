from flask import Flask, request, send_file
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
from flask import Flask, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
HF_TOKEN = os.getenv("HF_TOKEN")

@app.route("/")
def home():
    if HF_TOKEN:
        return "✅ Hugging Face Token Loaded Successfully!"
    else:
        return "❌ Token Not Found!"
    

   @app.route("/generate", methods=["POST"])
def generate():

    data = request.json
    prompt = data["prompt"]

    API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-dev"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    if response.status_code != 200:
        return response.text, response.status_code

    image_path = "../frontend/images/generated.png"

    with open(image_path, "wb") as f:
        f.write(response.content)

    return "Image Generated Successfully!"
if __name__ == "__main__":
    app.run(debug=True)