import random
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from models import Star, Planet, Civilization
from db import get_db

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:8000",
        "http://127.0.0.1:8080",
        "http://127.0.0.1:8000",
    ],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to ExoGenesis!"}


@app.post("/generate-galaxy")
async def generate_galaxy(db: AsyncSession = Depends(get_db), num_stars: int = 10):
    # Clear existing stars
    await db.execute(text("DELETE FROM planets"))
    await db.execute(text("DELETE FROM stars"))
    db.commit()

    # Generate stars
    stars = []
    for i in range(num_stars):
        star = Star(
            name=f"Star-{i}",
            type=random.choice(["G-type", "K-type", "M-type"]),
            x_position=random.uniform(-100, 100),
            y_position=random.uniform(-100, 100),
        )
        db.add(star)
        stars.append(star)

    await db.commit()  # Commit stars to generate IDs

    # Generate planets and civilizations
    for star in stars:
        for j in range(random.randint(1, 5)):
            planet = Planet(
                name=f"Planet-{star.id}-{j}",
                type=random.choice(["Rocky", "Gas Giant", "Icy"]),
                size=random.uniform(0.5, 3.0),  # Planet radius in arbitrary units
                orbital_distance=random.uniform(
                    0.1, 10.0
                ),  # Distance in arbitrary units
                star_id=star.id,
            )
            db.add(planet)

            if random.random() > 0.7:  # 30% chance of a civilization
                civ = Civilization(
                    name=f"Civ-{star.id}-{j}",
                    planet_id=planet.id,
                )
                db.add(civ)

    await db.commit()  # Commit planets and civilizations

    return {"message": "Galaxy generated successfully!"}


@app.get("/galaxy")
async def get_galaxy(db: AsyncSession = Depends(get_db)):
    # Fetch stars with their planets and civilizations
    query = await db.execute(
        text(
            "SELECT s.id AS star_id, s.name AS star_name, s.type AS star_type, s.x_position, s.y_position ,p.id AS planet_id, p.name AS planet_name, p.type AS planet_type, p.size, p.orbital_distance,c.id AS civ_id, c.name AS civ_name FROM stars s LEFT JOIN planets p ON s.id = p.star_id LEFT JOIN civilizations c ON p.id = c.planet_id"  # noqa: E501
        )
    )
    results = query.fetchall()

    # Structure the response
    galaxy = {}
    for row in results:
        star = galaxy.setdefault(
            row.star_id,
            {
                "name": row.star_name,
                "type": row.star_type,
                "x_position": row.x_position,
                "y_position": row.y_position,
                "planets": [],
            },
        )

        if row.planet_id:
            planet = {
                "id": row.planet_id,
                "name": row.planet_name,
                "type": row.planet_type,
                "size": row.size,
                "orbital_distance": row.orbital_distance,
                "civilization": None,
            }
            if row.civ_id:
                planet["civilization"] = {"id": row.civ_id, "name": row.civ_name}
            star["planets"].append(planet)

    return galaxy
