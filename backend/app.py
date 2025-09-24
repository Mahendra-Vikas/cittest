from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Backend is running on Render!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    user_input = data.get("input", "")
    # Example logic
    return jsonify({"output": f"You sent: {user_input}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
