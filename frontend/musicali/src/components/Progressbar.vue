<template>
<div class="progress-bar">
    <div class="progress-bar__fill" :style="{ width: progressPercentage + '%' }"></div>
  </div>

</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const progressPercentage = ref(0);
const currentPosition = ref(0);
const duration = ref(0);
let intervalId = null;

// Mock function to simulate getting playback state from Spotify API
async function getCurrentPlaybackState() {
  // Example API call to get the current playback state
  const response = await fetch('https://api.spotify.com/v1/me/player', {
    headers: {
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN', // Replace with your Spotify API token
    },
  });

  const data = await response.json();
  if (data && data.is_playing) {
    currentPosition.value = data.progress_ms;
    duration.value = data.item.duration_ms;
    progressPercentage.value = (currentPosition.value / duration.value) * 100;
  }
}

// Update the progress bar every second
onMounted(() => {
  intervalId = setInterval(async () => {
    await getCurrentPlaybackState();
  }, 1000);
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<style scoped>
.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #e0e0e0;
  border-radius: 5px;
  overflow: hidden;
}

.progress-bar__fill {
  height: 100%;
  background-color: #1db954; /* Spotify Green */
  transition: width 0.5s ease;
}
</style>