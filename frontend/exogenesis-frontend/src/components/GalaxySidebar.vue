<template>
  <aside :class="{ 'sidebar-open': isOpen }" class="galaxy-sidebar">
    <button class="toggle-button" @click="toggleSidebar">
      {{ isOpen ? 'Close' : 'Open' }}
    </button>
    <div v-if="isOpen" class="sidebar-content">
      <h2>Galaxy Overview</h2>
      <ul>
        <li>Total Stars: {{ galaxyStats.totalStars }}</li>
        <li>Total Planets: {{ galaxyStats.totalPlanets }}</li>
        <li>Star Types:</li>
        <ul>
          <li v-for="(count, type) in galaxyStats.starTypes" :key="type">
            {{ type }}: {{ count }}
          </li>
        </ul>
      </ul>
    </div>
  </aside>
</template>

<script>
export default {
  props: {
    galaxyStats: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isOpen: false,
    }
  },
  methods: {
    toggleSidebar() {
      this.isOpen = !this.isOpen
    },
  },
}
</script>

<style scoped>
.galaxy-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 250px;
  height: 100%;
  background-color: #222;
  color: #fff;
  padding: 1rem;
  overflow-y: auto;
  transition: transform 0.3s ease-in-out;
}

.galaxy-sidebar.collapsed {
  transform: translateX(-100%);
}
</style>
