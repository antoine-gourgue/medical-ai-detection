<template>
  <main class="min-h-screen bg-gray-50 py-16 px-4 sm:px-6 lg:px-16">
    <header class="text-center mb-16">
      <h1 class="text-5xl sm:text-6xl font-bold text-gray-700 mb-2">
        ZOIDBERG2.0
      </h1>
      <h2 class="text-4xl sm:text-5xl font-semibold text-gray-900 mb-2">
        Détection de Pneumonie
      </h2>
      <p class="text-gray-500 text-lg">
        Analyse d'images médicales assistée par l'intelligence artificielle
      </p>
    </header>

    <section class="flex flex-col items-center mb-20">
      <UploadForm
        @prediction="handlePrediction"
        @imageSelected="handleImageSelected"
        :disabled="hasAnalyzed"
      />

      <div v-if="previewImage && !hasAnalyzed" class="mt-10 w-full max-w-lg">
        <h2 class="text-lg font-medium text-gray-700 mb-4 text-center">Aperçu de l'image sélectionnée</h2>
        <div class="rounded-xl overflow-hidden border border-gray-200 shadow-sm">
          <img :src="previewImage" alt="Image sélectionnée" class="w-full object-cover" />
        </div>
      </div>
    </section>

    <section v-if="predictions.length" class="max-w-6xl mx-auto">
      <h2 class="text-2xl font-semibold text-gray-800 mb-10 text-center">
        Historique des analyses
      </h2>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
        <div
          v-for="(p, index) in predictions"
          :key="index"
          class="bg-white rounded-xl shadow-sm hover:shadow-md transition overflow-hidden"
        >
          <div class="aspect-w-4 aspect-h-3 bg-gray-100">
            <img :src="p.image" alt="Analyse" class="object-cover w-full h-full" />
          </div>
          <div class="p-5">
            <div class="flex justify-between items-center mb-3">
              <span class="text-sm text-gray-500">Type</span>
              <span class="font-medium text-gray-800">{{ p.label }}</span>
            </div>
            <div class="flex justify-between items-center mb-3">
              <span class="text-sm text-gray-500">Confiance</span>
              <span class="font-medium text-gray-800">{{ p.confidence }}%</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-sm text-gray-500">Raw</span>
              <code class="text-xs text-gray-600 bg-gray-100 px-2 py-0.5 rounded">
                {{ p.raw }}
              </code>
            </div>
            <div class="text-right text-xs text-gray-400 mt-4">
              {{ p.timestamp }}
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import UploadForm from './components/UploadForm.vue';

const predictions = ref([]);
const selectedImage = ref(null);
const previewImage = ref(null);
const hasAnalyzed = ref(false);

onMounted(() => {
  const saved = localStorage.getItem("predictions");
  if (saved) {
    predictions.value = JSON.parse(saved);
  }
});

const handleImageSelected = (imageFile) => {
  if (imageFile) {
    const reader = new FileReader();
    reader.onload = (e) => {
      selectedImage.value = imageFile;
      previewImage.value = e.target.result;
      hasAnalyzed.value = false;
    };
    reader.readAsDataURL(imageFile);
  }
};

const handlePrediction = (result) => {
  const prediction = {
    image: previewImage.value,
    raw: result.prediction,
    label: result.prediction >= 0.5 ? 'PNEUMONIA' : 'NORMAL',
    confidence: ((result.prediction >= 0.5 ? result.prediction : 1 - result.prediction) * 100).toFixed(2),
    timestamp: new Date().toLocaleString(),
  };

  predictions.value.unshift(prediction);
  localStorage.setItem("predictions", JSON.stringify(predictions.value));

  selectedImage.value = null;
  previewImage.value = null;
  hasAnalyzed.value = true;
};
</script>

<style scoped>
.aspect-w-4 {
  position: relative;
  width: 100%;
  padding-top: 75%;
}
.aspect-w-4 > img,
.aspect-w-4 > video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
