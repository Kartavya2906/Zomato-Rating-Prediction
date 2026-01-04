from flask import Flask, request, jsonify
import joblib
import numpy as np
import json
import os

app = Flask(__name__)

# # Load model & metadata
# model = joblib.load("../model/zomato_rating_model_rmse_0.321_20251229_0230.joblib")
# with open("../model/zomato_rating_model_metadata_20251229_0230.json") as f:
#     meta = json.load(f)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "model",
    "zomato_rating_model_rmse_0.321_20251229_0230.joblib"
)

META_PATH = os.path.join(
    BASE_DIR,
    "..",
    "model",
    "zomato_rating_model_metadata_20251229_0230.json"
)

model = joblib.load(MODEL_PATH)

with open(META_PATH, "r") as f:
    meta = json.load(f)

feature_order = meta["features"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_vector = [data.get(f, 0) for f in feature_order]
    prediction = model.predict([input_vector])[0]

    return jsonify({
        "predicted_rating": round(float(prediction), 2)
    })

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)
#not used in production deployment
# Use a WSGI server like Gunicorn to run the app in production