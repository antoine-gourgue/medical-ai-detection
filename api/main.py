import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import os


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static/uploads"
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/cnn_pneumonia_optimized.h5")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = tf.keras.models.load_model(MODEL_PATH)

IMG_SIZE = (64, 64)


def predict_pneumonia(image_path):
    img = Image.open(image_path).convert("L")
    img = img.resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = img.reshape(-1, 64, 64, 1)

    prediction = model.predict(img)[0][0]
    result = "PNEUMONIA" if prediction > 0.5 else "NORMAL"

    return result, float(prediction)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de détection de la pneumonie opérationnelle"}), 200


@app.route("/predict", methods=["POST"])
def upload_and_predict():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier envoyé"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nom de fichier vide"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    result, prediction = predict_pneumonia(file_path)

    return jsonify({"filename": filename, "result": result, "prediction": prediction}), 200


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5001)
