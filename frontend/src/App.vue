<script setup>
import { ref } from "vue";
import UploadForm from "./components/UploadForm.vue";

const prediction = ref(null);
const selectedImage = ref(null);

const handlePrediction = (result) => {
  prediction.value = result;
};

const handleImageSelected = (imageFile) => {
  if (imageFile) {
    const reader = new FileReader();
    reader.onload = (e) => {
      selectedImage.value = e.target.result;
    };
    reader.readAsDataURL(imageFile);
  }
};
</script>

<template>
  <div class="container">
    <h1>Détection de Pneumonie 🩺</h1>

    <div v-if="selectedImage" class="image-preview">
      <h2>Aperçu de l'image :</h2>
      <img :src="selectedImage" alt="Image sélectionnée" class="preview-img" />
    </div>

    <UploadForm @prediction="handlePrediction" @imageSelected="handleImageSelected" />

    <div v-if="prediction">
      <h2>Résultat de la prédiction :</h2>
      <p><strong>Type :</strong> {{ prediction.result }}</p>
      <p><strong>Prediction: {{prediction.prediction}}</strong></p>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 20px auto;
  text-align: center;
}

.image-preview {
  margin: 20px 0;
}

.preview-img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}
</style>
