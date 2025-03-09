import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.metrics import classification_report

# Charger les données
X_train = np.load("data/X_train.npy").reshape(-1, 64, 64, 1)  # Format CNN
Y_train = np.load("data/Y_train.npy")
X_test = np.load("data/X_test.npy").reshape(-1, 64, 64, 1)
Y_test = np.load("data/Y_test.npy")

# Définition du CNN amélioré
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(256, (3, 3), activation='relu'),  # Nouvelle couche
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),  # Ajout pour éviter l'overfitting
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')  # Sortie binaire
])

# Compilation et entraînement optimisé
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entraînement avec plus d'epochs (20)
model.fit(X_train, Y_train, epochs=20, batch_size=32, validation_split=0.2)

# Évaluation du modèle CNN
Y_pred = (model.predict(X_test) > 0.5).astype("int32")
accuracy = np.mean(Y_pred.flatten() == Y_test)
print(f"✅ Accuracy du modèle CNN : {accuracy:.4f}")
print(classification_report(Y_test, Y_pred))

# Sauvegarde du modèle optimisé
model.save("models/cnn_pneumonia_optimized.h5")
