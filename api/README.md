# 📌 API de Détection de Pneumonie avec Flask & TensorFlow

## 📖 Description
Cette API permet de détecter la pneumonie à partir d'images de radiographie en utilisant un modèle de deep learning entraîné avec TensorFlow/Keras. L'API expose une route permettant d'envoyer une image et de recevoir une prédiction indiquant si la radiographie est normale ou présente des signes de pneumonie.

---

## 🚀 Installation et Configuration

### 🔹 1. Cloner le projet
```bash
git clone https://github.com/votre-repo/medical-ai-detection.git
cd medical-ai-detection/api
```

### 🔹 2. Créer un environnement virtuel (Recommandé)
```bash
python3 -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate    # Sur Windows
```

### 🔹 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 🔹 4. Vérifier la présence du modèle entraîné
Assurez-vous que le modèle `cnn_pneumonia_optimized.h5` est bien présent dans le dossier `models/`. Sinon, exécutez l'entraînement du modèle avant de démarrer l'API.

```bash
ls models/
# Doit contenir: cnn_pneumonia_optimized.h5
```

---

## 🚀 Lancer l'API
Démarrez le serveur Flask avec :
```bash
python api/main.py
```

### 🎯 API accessible à :
📌 **URL principale** : `http://127.0.0.1:5001`

---

## 📌 Endpoints de l'API

### 🔹 **1. Prédiction d'une image**
- **URL** : `POST /predict`
- **Description** : Envoie une image de radiographie et reçoit une prédiction.
- **Format attendu** : FormData avec une clé `file` contenant une image (`.png`, `.jpg`, `.jpeg`)

#### 🛠 Exemple d'utilisation avec `cURL` :
```bash
curl -X POST -F "file=@chemin_vers_image.jpg" http://127.0.0.1:5001/predict
```

#### 📩 Réponse attendue (JSON) :
```json
{
    "prediction": "PNEUMONIA",  // ou "NORMAL"
    "confidence": 0.97  // Score de confiance entre 0 et 1
}
```

### 🔹 **2. Vérifier le statut de l'API**
- **URL** : `GET /health`
- **Description** : Vérifie que l'API fonctionne bien.

#### 📩 Réponse attendue :
```json
{
    "status": "API is running"
}
```

---

## 📌 Architecture du Backend

```
api/
│── models/
│   ├── cnn_pneumonia_optimized.h5   # Modèle entraîné
│── main.py                          # Code principal de l'API Flask
│── test_api.py                      # Script de test de l'API
│── requirements.txt                  # Dépendances Python
```

---

## 🛠 Débogage et Problèmes Courants

### 1️⃣ Port déjà occupé
Erreur :
```bash
Address already in use
Port 5000 is in use by another program.
```
Solution :
```bash
lsof -i :5000  # Trouver quel programme utilise le port
kill -9 <PID>  # Remplacez <PID> par l'ID du processus
```

### 2️⃣ Erreur "Model file not found"
Assurez-vous que le fichier `models/cnn_pneumonia_optimized.h5` existe.
Si nécessaire, exécutez à nouveau l'entraînement du modèle.

### 3️⃣ JSONDecodeError dans `test_api.py`
Vérifiez que le serveur est bien lancé avant d'envoyer une requête.
```bash
python api/main.py
```

---

