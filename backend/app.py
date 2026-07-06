from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "🚀 Kashi AI Studio Backend is Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data["prompt"]
    return f"You entered: {prompt}"

if __name__ == "__main__":
    app.run(debug=True)