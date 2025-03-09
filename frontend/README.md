# 🎨 Interface Web pour la Détection de Pneumonie

## 📖 Description
Cette interface web permet aux utilisateurs d'uploader une image de radiographie et d'obtenir une prédiction sur la présence ou non d'une pneumonie. Elle communique avec une API Flask qui exécute un modèle d'intelligence artificielle entraîné avec TensorFlow/Keras.

---

## 🚀 Installation et Configuration

### 🔹 1. Cloner le projet
```bash
git clone https://github.com/votre-repo/medical-ai-detection.git
cd medical-ai-detection/frontend
```

### 🔹 2. Installer les dépendances
```bash
npm install
```

### 🔹 3. Lancer le projet en mode développement
```bash
npm run dev
```
📌 **L'application sera accessible à** : `http://localhost:5173`

### 🔹 4. Construire le projet pour la production
```bash
npm run build
```

---

## 📌 Fonctionnalités
✅ Sélection d'une image de radiographie 📂
✅ Aperçu de l'image avant analyse 🖼
✅ Envoi de l'image à l'API backend pour prédiction 🔄
✅ Affichage du type détecté (Normal / Pneumonie) 🏥
✅ Indication de la confiance du modèle 🔢
✅ Interface responsive et intuitive 🎨

---

## 🏗 Architecture du Frontend

```
frontend/
│── src/
│   ├── components/
│   │   ├── UploadForm.vue       # Composant de téléversement de l'image
│   ├── App.vue                 # Composant principal
│   ├── main.js                 # Point d'entrée Vue.js
│── public/
│   ├── index.html              # Page HTML principale
│── package.json                # Dépendances du projet
│── vite.config.js              # Configuration Vite
```

---

## 📌 Détaillons les Composants

### 📂 `components/UploadForm.vue`
- Permet à l'utilisateur de sélectionner et d'envoyer une image
- Affiche un bouton "Analyser" pour déclencher la requête vers l'API
- Émet les événements `@prediction` et `@imageSelected`

### 📂 `App.vue`
- Récupère la prédiction de l'API et l'affiche
- Affiche l'image sélectionnée par l'utilisateur
- Organise le layout général de l'application

---

## 🛠 Dépannage et Erreurs Courantes

### 1️⃣ **Problème : API non accessible**
🔹 Vérifie que l'API est bien démarrée :
```bash
python api/main.py
```
🔹 Vérifie que l'URL de l'API est bien définie dans `UploadForm.vue` :
```js
const response = await fetch("http://127.0.0.1:5001/predict", {
  method: "POST",
  body: formData,
});
```

### 2️⃣ **Erreur `npm: command not found`**
🔹 Assurez-vous que Node.js et npm sont bien installés :
```bash
node -v
npm -v
```
🔹 Si npm n'est pas installé, téléchargez-le depuis [nodejs.org](https://nodejs.org/)

### 3️⃣ **Port déjà utilisé (`EADDRINUSE`)**
🔹 Vérifiez si un autre processus utilise le port 5173 :
```bash
lsof -i :5173
kill -9 <PID>  # Remplacez <PID> par l'ID du processus
```

---
