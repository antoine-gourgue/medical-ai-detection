import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../../data/chest_xray/")
IMG_SIZE = (128, 128)

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


def load_images_and_labels(dataset_path, augment=False):
    X, Y = [], []
    for category in ["NORMAL", "PNEUMONIA"]:
        path = os.path.join(dataset_path, category)
        label = 0 if category == "NORMAL" else 1
        for img_name in tqdm(os.listdir(path)[:1000]):
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, IMG_SIZE)
                img = np.expand_dims(img, axis=-1)

                if augment:
                    img = datagen.random_transform(img)

                X.append(img)
                Y.append(label)
    X = np.array(X) / 255.0
    Y = np.array(Y)
    return X, Y


X_train, Y_train = load_images_and_labels(os.path.join(DATASET_PATH, "train"), augment=True)
X_test, Y_test = load_images_and_labels(os.path.join(DATASET_PATH, "test"), augment=False)

X_train_cnn = X_train.reshape(-1, 128, 128, 1)
X_test_cnn = X_test.reshape(-1, 128, 128, 1)

X_train_knn = X_train.reshape(-1, 128 * 128)
X_test_knn = X_test.reshape(-1, 128 * 128)
