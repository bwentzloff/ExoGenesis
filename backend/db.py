import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
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
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session
