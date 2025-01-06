# README.md

## ExoGenesis

**Tagline:** Create. Expand. Endure.

ExoGenesis is an open-source procedural galaxy simulation designed to visualize the beauty of cosmic growth. Watch as civilizations evolve, expand, and endure across an expansive universe, driven by AI and procedurally generated environments.

---

### **Project Overview**
- **Purpose**: To simulate and visualize the dynamic expansion of galaxies and civilizations in real-time.
- **Key Features**:
  - Procedural galaxy generation (stars, planets, civilizations).
  - Real-time simulation of civilization growth and interactions.
  - Minimalist, 3D visualization using modern web technologies.
  - Open-source and extensible.

---

### **Getting Started**

#### **Prerequisites**
- **Backend**:
  - Python 3.9+
  - FastAPI
  - PostgreSQL
  - NumPy, SciPy
- **Frontend**:
  - Node.js 14+
  - Vue.js or React.js
  - Three.js

#### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/bwentzloff/ExoGenesis.git
   cd ExoGenesis
   ```
2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```
4. Run the simulation locally:
   ```bash
   # In backend/
   uvicorn main:app --reload

   # In frontend/
   npm run serve
   ```
5. Access the simulation at `http://localhost:3000`.

---

### **Project Structure**
- `frontend/`: Contains the Vue.js/React.js frontend.
- `backend/`: FastAPI backend logic and procedural generation code.
- `docs/`: Design documents, development plans, and other resources.
- `assets/`: Logos, visuals, and other media files.

---

### **Contributing**
We welcome contributions! Please refer to the `CONTRIBUTING.md` file for guidelines.

---

### **License**
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

---

### **Contact**
For questions, suggestions, or collaborations, feel free to open an issue or contact bwentzloff.

---

### **Acknowledgments**
Special thanks to the open-source community for tools and libraries that make ExoGenesis possible.