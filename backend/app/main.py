from fastapi import FastAPI
from app.database import engine, Base
from app.models import user            # ensure models are imported
from app.routers import auth           # your auth endpoints

Base.metadata.create_all(bind=engine)  # creates tables defined in models

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
