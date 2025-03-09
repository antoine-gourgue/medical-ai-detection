<script setup>
import { ref, defineEmits } from "vue";

const emit = defineEmits(["prediction", "imageSelected"]);
const selectedFile = ref(null);
const previewImage = ref(null);
const isLoading = ref(false);

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      previewImage.value = e.target.result;
      emit("imageSelected", file);
    };
    reader.readAsDataURL(file);
  }
};

const submitImage = async () => {
  if (!selectedFile.value) {
    alert("Veuillez sélectionner une image !");
    return;
  }

  isLoading.value = true;

  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await fetch("http://127.0.0.1:5001/predict", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    emit("prediction", result);
  } catch (error) {
    console.error("Erreur lors de la prédiction :", error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="upload-container">
    <label class="file-label">
      📂 Sélectionner une image
      <input type="file" @change="handleFileChange" accept="image/*" class="file-input" />
    </label>

    <button class="analyze-btn" @click="submitImage" :disabled="isLoading">
      {{ isLoading ? "Analyse en cours..." : "🔍 Analyser" }}
    </button>
  </div>
</template>

<style scoped>
.upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  width: 100%;
}

.file-label {
  display: inline-block;
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.file-input {
  display: none;
}

.analyze-btn {
  background-color: #28a745;
  color: white;
  padding: 12px 20px;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  max-width: 200px;
}

.analyze-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
