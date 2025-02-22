from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

# SQL Server connection string
DATABASE_URL = f"mssql+pyodbc://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_SERVER}/{Config.DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

# Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create a Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
