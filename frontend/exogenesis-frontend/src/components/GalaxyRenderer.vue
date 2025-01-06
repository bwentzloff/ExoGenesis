<template>
    <div>
      <h1>Galaxy Viewer</h1>
      <div v-if="loading">Loading galaxy data...</div>
      <div v-else-if="error">{{ error }}</div>
      <ul v-else>
        <li v-for="star in galaxy" :key="star.id">
          {{ star.name }} ({{ star.type }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getGalaxy } from "@/services/api";
  
  export default {
    data() {
      return {
        galaxy: [],
        loading: true,
        error: null,
      };
    },
    async created() {
      try {
        this.galaxy = await getGalaxy();
      } catch (err) {
        this.error = "Failed to load galaxy data.";
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  