import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.department import Department
from app.models.classroom import Classroom

def test_create_classroom(client: TestClient, auth_headers: dict, test_department: Department):
    """Test creating a new classroom"""
    classroom_data = {
        "building_name": "Science Building",
        "room_no": "S101",
        "capacity": 30,
        "department_id": test_department.id
    }
    response = client.post("/classroom/", json=classroom_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["building_name"] == "Science Building"
    assert data["room_no"] == "S101"
    assert data["capacity"] == 30
    assert data["department"]["id"] == test_department.id
    assert "id" in data

def test_create_classroom_invalid_department(client: TestClient, auth_headers: dict):
    """Test creating classroom with non-existent department"""
    classroom_data = {
        "building_name": "Engineering Building",
        "room_no": "E101",
        "capacity": 50,
        "department_id": 999  
    }
    response = client.post("/classroom/", json=classroom_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_create_classroom_unauthorized(client: TestClient, test_department: Department):
    """Test creating classroom without authentication"""
    classroom_data = {
        "building_name": "Engineering Building",
        "room_no": "E101",
        "capacity": 50,
        "department_id": test_department.id
    }
    response = client.post("/classroom/", json=classroom_data)
    assert response.status_code == 401

def test_get_classrooms(client: TestClient, auth_headers: dict, test_classroom: Classroom):
    """Test getting all classrooms"""
    response = client.get("/classroom/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(room["room_no"] == "E101" for room in data)

def test_get_classroom_by_id(client: TestClient, auth_headers: dict, test_classroom: Classroom):
    """Test getting classroom by ID"""
    response = client.get(f"/classroom/{test_classroom.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_classroom.id
    assert data["building_name"] == "Engineering Building"
    assert data["room_no"] == "E101"
    assert data["capacity"] == 50

def test_get_classroom_not_found(client: TestClient, auth_headers: dict):
    """Test getting non-existent classroom"""
    response = client.get("/classroom/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Classroom not found" in response.json()["detail"]

def test_update_classroom(client: TestClient, auth_headers: dict, test_classroom: Classroom, test_department: Department):
    """Test updating classroom"""
    update_data = {
        "building_name": "Updated Engineering Building",
        "room_no": "E102",
        "capacity": 60,
        "department_id": test_department.id
    }
    response = client.put(f"/classroom/{test_classroom.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["building_name"] == "Updated Engineering Building"
    assert data["room_no"] == "E102"
    assert data["capacity"] == 60
    assert data["id"] == test_classroom.id

def test_update_classroom_partial(client: TestClient, auth_headers: dict, test_classroom: Classroom):
    """Test partial update of classroom"""
    update_data = {
        "capacity": 75
        
    }
    response = client.put(f"/classroom/{test_classroom.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["capacity"] == 75
    assert data["building_name"] == "Engineering Building" 
    assert data["room_no"] == "E101" 

def test_update_classroom_invalid_department(client: TestClient, auth_headers: dict, test_classroom: Classroom):
    """Test updating classroom with invalid department"""
    update_data = {
        "building_name": "Updated Building",
        "room_no": "E103",
        "capacity": 40,
        "department_id": 999 
    }
    response = client.put(f"/classroom/{test_classroom.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_update_classroom_not_found(client: TestClient, auth_headers: dict, test_department: Department):
    """Test updating non-existent classroom"""
    update_data = {
        "building_name": "New Building",
        "room_no": "N101",
        "capacity": 40,
        "department_id": test_department.id
    }
    response = client.put("/classroom/999", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Classroom not found" in response.json()["detail"]

def test_delete_classroom(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test deleting classroom"""
    
    from app.models.classroom import Classroom
    classroom = Classroom(
        building_name="Temporary Building",
        room_no="T101",
        capacity=25,
        department_id=test_department.id
    )
    session.add(classroom)
    session.commit()
    session.refresh(classroom)
    
    response = client.delete(f"/classroom/{classroom.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Classroom deleted successfully"
    assert data["data"]["id"] == classroom.id

    # Verify classroom is deleted
    response = client.get(f"/classroom/{classroom.id}", headers=auth_headers)
    assert response.status_code == 404

def test_delete_classroom_not_found(client: TestClient, auth_headers: dict):
    """Test deleting non-existent classroom"""
    response = client.delete("/classroom/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Classroom not found" in response.json()["detail"]

def test_classroom_unauthorized_access(client: TestClient, test_classroom: Classroom):
    """Test accessing classroom endpoints without authentication"""
    
    response = client.get("/classroom/")
    assert response.status_code == 401
    
    
    response = client.get(f"/classroom/{test_classroom.id}")
    assert response.status_code == 401
    
    
    response = client.put(f"/classroom/{test_classroom.id}", json={"capacity": 100})
    assert response.status_code == 401
    
    
    response = client.delete(f"/classroom/{test_classroom.id}")
    assert response.status_code == 401
