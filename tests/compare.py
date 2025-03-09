import numpy as np
from sklearn.metrics import classification_report
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier

# Charger les données
X_test_flat = np.load("data/X_test.npy").reshape(-1, 64 * 64)
Y_test = np.load("data/Y_test.npy")

# Charger et tester KNN
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(np.load("data/X_train.npy").reshape(-1, 64 * 64), np.load("data/Y_train.npy"))
Y_pred_knn = knn.predict(X_test_flat)

# Charger et tester CNN
cnn = tf.keras.models.load_model("models/cnn_pneumonia.h5")
Y_pred_cnn = (cnn.predict(np.load("data/X_test.npy").reshape(-1, 64, 64, 1)) > 0.5).astype("int32").flatten()

# Résultats
print("\n🔍 **KNN Performance**")
print(classification_report(Y_test, Y_pred_knn))

print("\n🧠 **CNN Performance**")
print(classification_report(Y_test, Y_pred_cnn))
