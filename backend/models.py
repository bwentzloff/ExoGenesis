from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Star(Base):
    __tablename__ = "stars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    x_position = Column(Float, nullable=False)
    y_position = Column(Float, nullable=False)

    planets = relationship("Planet", back_populates="star")


class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    star_id = Column(Integer, ForeignKey("stars.id"))
    star = relationship("Star", back_populates="planets")
    size = Column(Float, nullable=False)  # Represented as a radius
    orbital_distance = Column(Float, nullable=False)  # Distance from star

    civilizations = relationship("Civilization", back_populates="planet")


class Civilization(Base):
    __tablename__ = "civilizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    planet_id = Column(Integer, ForeignKey("planets.id"))
    planet = relationship("Planet", back_populates="civilizations")
