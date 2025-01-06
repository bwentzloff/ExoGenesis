# Contributing to ExoGenesis

Thank you for your interest in contributing to ExoGenesis! 🎉 This project aims to create a visually stunning and interactive galaxy simulation that is open-source and community-driven. Contributions from developers, designers, and testers are always welcome!

To get started, please follow the guidelines below to ensure a smooth collaboration.

---

## 🚀 How to Contribute

### 1. File an Issue
If you encounter a bug or have a feature request, start by filing an issue on the [GitHub Issues page](https://github.com/bwentzloff/ExoGenesis/issues).
- Clearly describe the problem or suggestion.
- Include steps to reproduce the issue (if applicable).

### 2. Propose Features
Have an idea? Start a discussion in the **Issues** section or reach out via pull request with a detailed proposal.

### 3. Fix Bugs or Add Features
Browse the [open issues](https://github.com/bwentzloff/ExoGenesis/issues) or check the [GitHub Project Board](https://github.com/bwentzloff/ExoGenesis/projects) for tasks marked as `good first issue` or `help wanted`.

---

## 🛠️ Development Setup

Follow these steps to set up the project locally.

### Prerequisites
- **Node.js** (latest LTS version recommended)
- **Python 3.8+**
- **PostgreSQL**

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/bwentzloff/ExoGenesis.git
   cd ExoGenesis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   alembic upgrade head
   ```

5. Start the backend:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run serve
   ```

---

## 🧹 Coding Guidelines

### Linting and Formatting
- **Frontend**: Use `eslint` and `prettier` to ensure consistent formatting.
- **Backend**: Use `black` for formatting and `flake8` for linting.

Run the following commands before committing changes:
- Frontend:
  ```bash
  npm run lint
  ```
- Backend:
  ```bash
  black . && flake8
  ```

### Testing
All new features and fixes should include tests:
- **Frontend**: Add tests using `Jest`.
- **Backend**: Add tests using `pytest`.

Run the test suite:
- Frontend:
  ```bash
  npm run test
  ```
- Backend:
  ```bash
  pytest
  ```

---

## ✅ Submitting Changes

### Branching Strategy
1. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Push your changes to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Checklist
Before opening a pull request, ensure that:
- Your changes adhere to the coding guidelines.
- All tests pass locally.
- You have added relevant documentation.

Open a pull request and describe your changes in detail.

---

## 📜 Code of Conduct
We expect all contributors to adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md). Please be respectful and inclusive.

---

## 💖 Acknowledgments
Thank you for contributing to ExoGenesis! Your support makes this project better for everyone.

Happy coding! 🌌