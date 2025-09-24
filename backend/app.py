from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow all origins (for hackathon demo)
CORS(app)

@app.route("/")
def home():
    return {"message": "Backend is running on Render!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json or {}
    user_input = data.get("input", "")
    # Example logic: reverse the input
    result = user_input[::-1]
    return jsonify({"output": f"Processed: {result}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
