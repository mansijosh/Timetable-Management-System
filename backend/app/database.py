from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# single shared engine
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for all ORM models
Base = declarative_base()

# FastAPI dependency you’ll use in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
