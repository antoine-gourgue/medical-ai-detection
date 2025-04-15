import numpy as np
from sklearn.metrics import classification_report
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier

X_test_flat = np.load("data/X_test.npy").reshape(-1, 256 * 256)
Y_test = np.load("data/Y_test.npy")

knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(np.load("data/X_train.npy").reshape(-1, 256 * 256), np.load("data/Y_train.npy"))
Y_pred_knn = knn.predict(X_test_flat)

cnn = tf.keras.models.load_model("models/cnn_pneumonia.h5")
Y_pred_cnn = (cnn.predict(np.load("data/X_test.npy").reshape(-1, 256, 256, 1)) > 0.5).astype("int32").flatten()

print("\n🔍 **KNN Performance**")
print(classification_report(Y_test, Y_pred_knn))

print("\n🧠 **CNN Performance**")
print(classification_report(Y_test, Y_pred_cnn))
