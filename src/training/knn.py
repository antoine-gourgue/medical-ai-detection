import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# 📂 Vérifier si les fichiers existent avant chargement
DATA_DIR = "data/"
files = ["X_train.npy", "Y_train.npy", "X_test.npy", "Y_test.npy"]

for file in files:
    if not os.path.exists(os.path.join(DATA_DIR, file)):
        raise FileNotFoundError(f"❌ Erreur : Le fichier '{file}' est introuvable dans {DATA_DIR}")

# ✅ Charger les données
X_train = np.load(os.path.join(DATA_DIR, "X_train.npy"))  # (N, 64, 64)
Y_train = np.load(os.path.join(DATA_DIR, "Y_train.npy"))
X_test = np.load(os.path.join(DATA_DIR, "X_test.npy"))
Y_test = np.load(os.path.join(DATA_DIR, "Y_test.npy"))

# ✅ Vérifier les dimensions des données après chargement
print("\n📊 Vérification des tailles des données après chargement :")
print(f"X_train shape: {X_train.shape}")
print(f"Y_train shape: {Y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"Y_test shape: {Y_test.shape}")

# ✅ Correction du format des labels (évite ValueError)
Y_train = Y_train.ravel()
Y_test = Y_test.ravel()

# ✅ Vérification de la cohérence
if X_train.shape[0] != Y_train.shape[0] or X_test.shape[0] != Y_test.shape[0]:
    raise ValueError(f"❌ Erreur : Mismatch entre X et Y. {X_train.shape[0]} images mais {Y_train.shape[0]} labels.")

# ✅ Aplatir les images pour KNN
X_train_knn = X_train.reshape(-1, 64 * 64)
X_test_knn = X_test.reshape(-1, 64 * 64)

# ✅ Normalisation des données
scaler = StandardScaler()
X_train_knn = scaler.fit_transform(X_train_knn)
X_test_knn = scaler.transform(X_test_knn)

# ✅ Entraîner le modèle KNN optimisé
print("\n🚀 Entraînement du modèle KNN...")
print("📊 Vérification des tailles avant entraînement KNN :")
print(f"X_train_knn shape: {X_train_knn.shape}")
print(f"Y_train shape: {Y_train.shape}")

knn = KNeighborsClassifier(n_neighbors=7, metric='manhattan', weights='distance')
knn.fit(X_train_knn, Y_train)

# ✅ Prédictions et évaluation
Y_pred = knn.predict(X_test_knn)
accuracy = accuracy_score(Y_test, Y_pred)

print(f"\n✅ Accuracy du modèle KNN : {accuracy:.4f}")
print("\n📊 Rapport de classification :\n", classification_report(Y_test, Y_pred))
