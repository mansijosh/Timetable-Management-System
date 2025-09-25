from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import  department
from app.routers import  classroom
from app.routers import auth
from app.middleware import add_timing_middleware  
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_timing_middleware(app)

# Create tables at startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["User"])
app.include_router(department.router, prefix="/department", tags=["Department"])
app.include_router(classroom.router, prefix="/classroom", tags=["classroom"])