<template>
    <div ref="rendererContainer" style="width: 100%; height: 100%;"></div>
  </template>
  
  <script>
  import * as THREE from "three";
  import { onBeforeUnmount } from "vue";
  
  export default {
    props: {
      galaxy: {
        type: Array,
        required: true,
      },
    },
    mounted() {
        const plainGalaxy = JSON.parse(JSON.stringify(this.galaxy)); // Convert to plain array
  console.log("Converted galaxy data:", plainGalaxy);
      // Three.js objects declared as regular variables
      let scene, camera, renderer;
  
      const initThreeJS = () => {
        // Create Scene
        scene = new THREE.Scene();
  
        // Create Camera
        camera = new THREE.PerspectiveCamera(
          75, // Field of view
          this.$refs.rendererContainer.clientWidth / this.$refs.rendererContainer.clientHeight, // Aspect ratio
          0.1, // Near clipping plane
          1000 // Far clipping plane
        );
        camera.position.z = 200;
  
        // Create Renderer
        renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(
          this.$refs.rendererContainer.clientWidth,
          this.$refs.rendererContainer.clientHeight
        );
        this.$refs.rendererContainer.appendChild(renderer.domElement);
  
        // Add Stars (using a plain array)
        this.galaxy.forEach((star, index) => {
          const starGeometry = new THREE.SphereGeometry(3, 16, 16);
          const starMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00 });
          const starMesh = new THREE.Mesh(starGeometry, starMaterial);
  
          // Position stars
          starMesh.position.set(
            star.x_position || Math.random() * 200 - 100,
            star.y_position || Math.random() * 200 - 100,
            0
          );
  
          console.log(`Adding star ${index} to scene at position:`, starMesh.position);
          scene.add(starMesh);
        });
  
        // Render Loop
        const animate = () => {
          requestAnimationFrame(animate);
          renderer.render(scene, camera);
        };
        animate();
      };
  
      // Initialize Three.js after component mounts
      initThreeJS();
  
      // Cleanup resources on unmount
      onBeforeUnmount(() => {
        renderer.dispose();
        scene = null;
        camera = null;
        renderer = null;
      });
    },
  };
  </script>
  
  <style>
  div {
    display: block;
  }
  </style>
  