
# Galactic Simulation: Technical Details and Tech Stack

## Finalized Tech Stack

### 1. Frontend
- **Framework**:
  - **Vue.js** or **React.js** (whichever aligns better with team familiarity and tooling).
  - **Three.js**: For rendering the 3D galaxy map and visualizing stars, planets, and territories.

- **Visualization Tools**:
  - **CSS/Canvas/Three.js**: For glowing effects, animations, and dynamic elements.
  - **D3.js**: For advanced visualizations, such as trade routes or event overlays (if needed).

---

### 2. Backend
- **Language**: Python.
- **Framework**: FastAPI for API development, real-time WebSocket communication, and async support.
- **Database**:
  - **PostgreSQL**: For storing galaxy data (stars, planets, civilizations).
  - **Redis**: For caching real-time simulation states, ensuring smooth performance.

---

### 3. Procedural Generation
- **Algorithm**:
  - Use Perlin noise and seeded random generation for galaxy layout and star distribution.
- **Libraries**:
  - **NumPy**: For handling array-based galaxy computations.
  - **SciPy**: For advanced mathematical operations in procedural algorithms.

---

### 4. Real-Time Simulation
- **Simulation Logic**:
  - Written in Python for civilization expansion, AI behaviors, and event triggers.
- **Frontend Communication**:
  - WebSocket API to push updates and ensure synchronization between backend and frontend.

---

### 5. Hosting and Deployment
- **Frontend Hosting**:
  - **Netlify** or **Vercel** for ease of deployment and CI/CD integration.
- **Backend Hosting**:
  - **AWS Lambda** or **Google Cloud Run** for scalable, serverless backend services.

---

### 6. Open Source and Collaboration
- **Version Control**: GitHub, with clear contribution guidelines and issue tracking.
- **Documentation**:
  - Markdown files for setup, contribution, and code explanations.
  - Optional use of ReadTheDocs for dynamic, hosted documentation.
- **Modular Code**:
  - Components and modules designed for ease of understanding and extension.

---

This finalized stack ensures scalability, modularity, and a clear path for open-source contributions from day one.
