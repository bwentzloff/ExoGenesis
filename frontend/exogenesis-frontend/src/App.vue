<template>
  <div id="app">
    <div v-if="loading">Loading galaxy...</div>
    <Galaxy3D v-else :galaxy="galaxyData" />
  </div>
</template>

<script>
import Galaxy3D from '@/components/Galaxy3D'
import { getGalaxy } from '@/services/api'

export default {
  components: {
    Galaxy3D,
  },
  data() {
    return {
      galaxyData: [], // Initialize as an empty array
      loading: true,
    }
  },
  async created() {
    try {
      const galaxyObject = await getGalaxy()
      this.galaxyData = Object.values(galaxyObject)
      console.log('Galaxy data in App.vue after fetching:', this.galaxyData)
    } catch (error) {
      console.error('Failed to fetch galaxy data:', error)
    } finally {
      this.loading = false
    }
  },
}
</script>

<style>
#app {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
</style>
