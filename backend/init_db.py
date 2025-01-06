import os
from sqlalchemy.ext.asyncio import create_async_engine
from models import Base
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection settings
DB_USER = os.getenv("EXOGENESIS_DB_USER")
DB_PASSWORD = os.getenv("EXOGENESIS_DB_PASSWORD")
DB_HOST = os.getenv("EXOGENESIS_DB_HOST")
DB_NAME = os.getenv("EXOGENESIS_DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())
