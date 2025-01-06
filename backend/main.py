from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to ExoGenesis!"}

@app.get("/generate-galaxy")
def generate_galaxy():
    # Placeholder data
    return {
        "stars": [{"id": 1, "type": "G-type", "position": [0, 0]}],
        "planets": [{"id": 1, "star_id": 1, "type": "Rocky"}],
        "civilizations": [{"id": 1, "planet_id": 1, "name": "Alpha Centauri"}],
    }
