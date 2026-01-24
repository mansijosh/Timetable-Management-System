import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.department import Department

def test_create_department(client: TestClient, auth_headers: dict):
    """Test creating a new department"""
    department_data = {
        "name": "Mathematics",
        "year": 2024
    }
    response = client.post("/department/", json=department_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Mathematics"
    assert data["year"] == 2024
    assert "id" in data

def test_create_department_duplicate_name(client: TestClient, auth_headers: dict, test_department: Department):
    """Test creating department with duplicate name"""
    department_data = {
        "name": "Computer Science",  # Same as test_department
        "year": 2025
    }
    response = client.post("/department/", json=department_data, headers=auth_headers)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"].lower()

def test_create_department_unauthorized(client: TestClient):
    """Test creating department without authentication"""
    department_data = {
        "name": "Physics",
        "year": 2024
    }
    response = client.post("/department/", json=department_data)
    assert response.status_code == 401

def test_get_departments(client: TestClient, auth_headers: dict, test_department: Department):
    """Test getting all departments"""
    response = client.get("/department/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(dept["name"] == "Computer Science" for dept in data)

def test_get_department_by_id(client: TestClient, auth_headers: dict, test_department: Department):
    """Test getting department by ID"""
    response = client.get(f"/department/{test_department.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_department.id
    assert data["name"] == "Computer Science"
    assert data["year"] == 2024

def test_get_department_not_found(client: TestClient, auth_headers: dict):
    """Test getting non-existent department"""
    response = client.get("/department/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_update_department(client: TestClient, auth_headers: dict, test_department: Department):
    """Test updating department"""
    update_data = {
        "name": "Advanced Computer Science",
        "year": 2025
    }
    response = client.put(f"/department/{test_department.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Computer Science"
    assert data["year"] == 2025
    assert data["id"] == test_department.id

def test_update_department_partial(client: TestClient, auth_headers: dict, test_department: Department):
    """Test partial update of department"""
    update_data = {
        "name": "Updated Computer Science"
        # year not provided, should remain unchanged
    }
    response = client.put(f"/department/{test_department.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Computer Science"
    assert data["year"] == 2024  # Original year should remain

def test_update_department_not_found(client: TestClient, auth_headers: dict):
    """Test updating non-existent department"""
    update_data = {
        "name": "Physics",
        "year": 2024
    }
    response = client.put("/department/999", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_delete_department(client: TestClient, auth_headers: dict, session: Session):
    """Test deleting department"""
   
    from app.models.department import Department
    department = Department(name="Physics", year=2024)
    session.add(department)
    session.commit()
    session.refresh(department)
    
    response = client.delete(f"/department/{department.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Department deleted successfully"
    assert data["data"]["id"] == department.id
    
    # Verify department is deleted
    response = client.get(f"/department/{department.id}", headers=auth_headers)
    assert response.status_code == 404

def test_delete_department_not_found(client: TestClient, auth_headers: dict):
    """Test deleting non-existent department"""
    response = client.delete("/department/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_department_unauthorized_access(client: TestClient, test_department: Department):
    """Test accessing department endpoints without authentication"""
    # Test GET without auth
    response = client.get("/department/")
    assert response.status_code == 401
    
    # Test GET by ID without auth
    response = client.get(f"/department/{test_department.id}")
    assert response.status_code == 401
    
    # Test PUT without auth
    response = client.put(f"/department/{test_department.id}", json={"name": "Updated"})
    assert response.status_code == 401
    
    # Test DELETE without auth
    response = client.delete(f"/department/{test_department.id}")
    assert response.status_code == 401
