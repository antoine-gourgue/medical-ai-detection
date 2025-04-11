<template>
  <div class="w-full max-w-md flex flex-col items-center gap-6">
    <label
      class="w-full text-center cursor-pointer px-6 py-4 bg-white border border-gray-300 rounded-xl shadow-sm hover:border-gray-400 transition"
    >
      <span class="text-gray-700 font-medium">Sélectionner une image</span>
      <input
        type="file"
        @change="handleFileChange"
        accept="image/*"
        class="hidden"
      />
    </label>

    <button
      @click="submitImage"
      :disabled="isLoading || hasAnalyzed"
      class="w-full px-6 py-3 bg-gray-900 text-white font-medium rounded-xl shadow-sm hover:bg-gray-800 transition disabled:opacity-50"
    >
      {{ isLoading ? "Analyse en cours..." : "Analyser l'image" }}
    </button>
  </div>
</template>

<script setup>
import { ref, defineEmits, watch } from "vue";

const emit = defineEmits(["prediction", "imageSelected"]);
const selectedFile = ref(null);
const isLoading = ref(false);
const hasAnalyzed = ref(false);

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
    hasAnalyzed.value = false;
    emit("imageSelected", file);
  }
};

const submitImage = async () => {
  if (!selectedFile.value || hasAnalyzed.value) return;

  isLoading.value = true;
  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/predict`, {
      method: "POST",
      body: formData,
    });
    const result = await response.json();
    emit("prediction", result);
    hasAnalyzed.value = true;
  } catch (error) {
    console.error("Erreur lors de la prédiction :", error);
  } finally {
    isLoading.value = false;
  }
};
</script>