import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.user import User
from app.models.roles import Role

def test_register_user(client: TestClient, session: Session):
    """Test user registration"""
    role = Role(role_name="user")
    session.add(role)
    session.commit()
    session.refresh(role)
    
    user_data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "phone_number": "1234567890",
        "password": "newpassword123",
        "role_id": role.id
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert data["phone_number"] == "1234567890"
    # assert data["role_id"] == role.id
    assert "id" in data

def test_register_duplicate_username(client: TestClient, test_user: User):
    """Test registration with duplicate username"""
    user_data = {
        "username": "testuser",
        "email": "different@example.com",
        "phone_number": "1234567890",
        "password": "password123"
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 400
    assert "Username already registered" in response.json()["detail"]

def test_register_duplicate_email(client: TestClient, test_user: User):
    """Test registration with duplicate email"""
    user_data = {
        "username": "differentuser",
        "email": "test@example.com",
        "phone_number": "8888888888",  
        "password": "password123"
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]

def test_login_success(client: TestClient, test_user: User):
    """Test successful login"""
    login_data = {
        "username": "test@example.com",
        "password": "testpassword123"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client: TestClient, test_user: User):
    """Test login with invalid credentials"""
    login_data = {
        "username": "test@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 401
    assert "Invalid credentials" in response.json()["detail"]

def test_login_nonexistent_user(client: TestClient):
    """Test login with non-existent user"""
    login_data = {
        "username": "nonexistent",
        "password": "password123"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 401
    assert "Invalid credentials" in response.json()["detail"]

def test_login_json_format(client: TestClient, test_user: User):
    """Test login with JSON format (should return 422 since endpoint expects form data)"""
    login_data = {
        "username": "test@example.com",
        "password": "testpassword123"
    }
    response = client.post("/auth/login", json=login_data)
    # Login endpoint expects form data, not JSON
    assert response.status_code == 422

def test_password_length_handling(client: TestClient):
    """Test password with length > 72 characters (should work with Argon2)"""
    long_password = "a" * 100  # 100 character password
    user_data = {
        "username": "longpassuser",
        "email": "longpass@example.com",
        "phone_number": "7777777777",
        "password": long_password
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    
    # Test login with the same long password
    login_data = {
        "username": "longpass@example.com",
        "password": long_password
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
