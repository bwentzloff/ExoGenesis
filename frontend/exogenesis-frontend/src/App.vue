<template>
  <div id="app">
    <div v-if="loading">Loading galaxy...</div>
    <Galaxy3D v-else :galaxy="galaxyData" />
    <GalaxySidebar :galaxyStats="galaxyStats" />
  </div>
</template>

<script>
import Galaxy3D from '@/components/Galaxy3D'
import GalaxySidebar from './components/GalaxySidebar.vue'
import { getGalaxy } from '@/services/api'

export default {
  components: {
    Galaxy3D,
    GalaxySidebar,
  },
  data() {
    return {
      galaxyData: [], // Initialize as an empty array
      loading: true,
      galaxyStats: {
        totalStars: 0,
        totalPlanets: 0,
        starTypes: {},
      },
    }
  },
  methods: {
    fetchGalaxyData() {
      fetch('http://127.0.0.1:8000/galaxy')
        .then((response) => response.json())
        .then((data) => {
          this.galaxyData = Array.isArray(data) ? data : data.galaxy || []; // Adjust for potential object wrapping
          this.updateGalaxyStats()
        })
    },
    updateGalaxyStats() {
      const starTypes = {}
      let totalPlanets = 0
      this.galaxyData.forEach((star) => {
        starTypes[star.type] = (starTypes[star.type] || 0) + 1
        totalPlanets += star.planets.length
      })
      this.galaxyStats = {
        totalStars: this.galaxyData.length,
        totalPlanets,
        starTypes,
      }
    },
  },
  mounted() {
    this.fetchGalaxyData()
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
