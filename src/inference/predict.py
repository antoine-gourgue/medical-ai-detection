import numpy as np
import os
import cv2
import tensorflow as tf

model = tf.keras.models.load_model("models/cnn_pneumonia.h5")

def predict_pneumonia(image_path):
    IMG_SIZE = (64, 64)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMG_SIZE)
    img = img / 255.0
    img = img.reshape(-1, 64, 64, 1)

    prediction = model.predict(img)[0][0]
    if prediction > 0.5:
        return "PNEUMONIA detected! ⚠️"
    else:
        return "NORMAL lungs ✅"

image_path = os.path.join(os.path.dirname(__file__), "../../data/chest_xray/test/NORMAL/IM-0001-0001.jpeg")
print(predict_pneumonia(image_path))
