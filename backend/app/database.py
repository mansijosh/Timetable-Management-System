from sqlmodel import SQLModel, create_engine, Session
from app.config import settings

# Create the engine
engine = create_engine(settings.DATABASE_URL, echo=True)

# Create DB tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# FastAPI dependency
def get_db():
    with Session(engine) as session:
        yield session
