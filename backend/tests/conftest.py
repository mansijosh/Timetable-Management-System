import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
import tempfile
import os
from app.config import settings

from app.main import app
from app.database import get_db
from app.models.user import User
from app.models.department import Department
from app.models.classroom import Classroom
from app.crud.user import create_user
from app.schemas.user import UserCreate
from app.models.roles import Role

# Create a test database for testing (using PostgreSQL)
@pytest.fixture(name="session")
def session_fixture():
    # Use test database URL or fallback to in-memory SQLite for CI
    test_db_url = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")
    
    if test_db_url.startswith("sqlite"):
        # SQLite configuration for CI/fallback
        engine = create_engine(
            test_db_url,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
    else:
        # PostgreSQL configuration
        engine = create_engine(test_db_url)
    
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture(autouse=True)
def setup_database(session: Session):
    """Ensure database is clean and set up for each test"""
    # Clear all tables
    for table in reversed(SQLModel.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
    
    # Create tables
    SQLModel.metadata.create_all(session.bind)
    yield
    # Cleanup after test
    for table in reversed(SQLModel.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()

@pytest.fixture(name="test_role")
def test_role_fixture(session: Session):
    role = Role(role_name="user")
    session.add(role)
    session.commit()
    session.refresh(role)
    return role

@pytest.fixture(name="test_user")
def test_user_fixture(session: Session, test_role):
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        phone_number="999999999",
        password="testpassword123"
    )
    user = create_user(session, user_data, role_id=test_role.id)
    return user

@pytest.fixture(name="test_department")
def test_department_fixture(session: Session):
    department = Department(name="Computer Science", year=2024)
    session.add(department)
    session.commit()
    session.refresh(department)
    return department

@pytest.fixture(name="test_classroom")
def test_classroom_fixture(session: Session, test_department: Department):
    classroom = Classroom(
        building_name="Engineering Building",
        room_no="E101",
        capacity=50,
        department_id=test_department.id
    )
    session.add(classroom)
    session.commit()
    session.refresh(classroom)
    return classroom

@pytest.fixture(name="auth_headers")
def auth_headers_fixture(client: TestClient, test_user: User):
    # Login to get token
    response = client.post(
        "/auth/login",
        data={"username": "testuser", "password": "testpassword123"}
    )
    
    assert response.status_code == 200
    
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
