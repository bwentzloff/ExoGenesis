<template>
  <div ref="rendererContainer" style="width: 100%; height: 100%"></div>
</template>

<script>
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { onBeforeUnmount } from 'vue'

export default {
  props: {
    galaxy: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      controls: null, // Declare the controls property
    }
  },
  mounted() {
    // Three.js objects declared as regular variables
    let scene, camera, renderer

    const initThreeJS = () => {
      // Create Scene
      scene = new THREE.Scene()

      // Create Camera
      camera = new THREE.PerspectiveCamera(
        75, // Field of view
        this.$refs.rendererContainer.clientWidth /
          this.$refs.rendererContainer.clientHeight, // Aspect ratio
        0.1, // Near clipping plane
        1000, // Far clipping plane
      )
      camera.position.z = 200

      // Create Renderer
      renderer = new THREE.WebGLRenderer({ antialias: true })
      renderer.setSize(
        this.$refs.rendererContainer.clientWidth,
        this.$refs.rendererContainer.clientHeight,
      )
      this.$refs.rendererContainer.appendChild(renderer.domElement)

      // Add Stars (using a plain array)
      this.galaxy.forEach((star) => {
        const starColors = {
          O: 0x9bb0ff, // Blue
          B: 0xaabfff, // Blue-white
          A: 0xcad7ff, // White
          F: 0xf8f7ff, // Yellow-white
          G: 0xfff4e8, // Yellow
          K: 0x9bb0ff, // Blue
          M: 0xffaa80, // Red
        }
        const color = starColors[star.type.charAt(0).toUpperCase()] || 0xffffff
        const starGeometry = new THREE.SphereGeometry(3, 16, 16)
        const starMaterial = new THREE.MeshBasicMaterial({ color: color })
        const starMesh = new THREE.Mesh(starGeometry, starMaterial)

        // Position stars
        starMesh.position.set(star.x_position, star.y_position, 0)

        scene.add(starMesh)
        // Add planets for this star
        star.planets.forEach((planet) => {
          const planetGeometry = new THREE.SphereGeometry(
            planet.size / 5,
            16,
            16,
          )
          const planetMaterial = new THREE.MeshBasicMaterial({
            color: 0x00ff00,
          })
          const planetMesh = new THREE.Mesh(planetGeometry, planetMaterial)

          planetMesh.position.set(
            star.x_position + planet.orbital_distance,
            star.y_position,
            0,
          )
          scene.add(planetMesh)
        })
      })

      // Render Loop
      const animate = () => {
        requestAnimationFrame(animate)
        if (this.controls) {
          this.controls.update() // Ensure controls are updated for damping
        }
        renderer.render(scene, camera)
      }
      this.controls = new OrbitControls(camera, renderer.domElement)
      this.controls.enableDamping = true
      this.controls.dampingFactor = 0.05
      this.controls.minDistance = 50
      this.controls.maxDistance = 1000
      animate()
    }

    // Initialize Three.js after component mounts
    initThreeJS()
    //this.initOrbitControls();

    // Cleanup resources on unmount
    onBeforeUnmount(() => {
      renderer.dispose()
      scene = null
      camera = null
      renderer = null
    })
  },
}
</script>

<style>
div {
  display: block;
}
</style>
