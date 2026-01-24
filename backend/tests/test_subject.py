import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.subject import Subject

def test_create_subject(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test creating a new subject"""
   
    from app.models.faculty import Faculty
    faculty = Faculty(name="Dr. Subject Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject_data = {
        "name": "Advanced Mathematics",
        "faculty_id": faculty.id,
        "department_id": test_department.id
    }
    response = client.post("/subject/", json=subject_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Advanced Mathematics"
    assert data["faculty"]["id"] == faculty.id
    assert data["department"]["id"] == test_department.id
    assert "id" in data

def test_create_subject_invalid_faculty(client: TestClient, auth_headers: dict, test_department: Department):
    """Test creating subject with non-existent faculty"""
    subject_data = {
        "name": "Test Subject",
        "faculty_id": 999,  
        "department_id": test_department.id
    }
    response = client.post("/subject/", json=subject_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Faculty not found" in response.json()["detail"]

def test_create_subject_invalid_department(client: TestClient, auth_headers: dict, session: Session):
    """Test creating subject with non-existent department"""
    from app.models.faculty import Faculty
    faculty = Faculty(name="Dr. Test Professor", department_id=1) 
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject_data = {
        "name": "Test Subject",
        "faculty_id": faculty.id,
        "department_id": 999  
    }
    response = client.post("/subject/", json=subject_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]

def test_create_subject_unauthorized(client: TestClient, session: Session, test_department: Department):
    """Test creating subject without authentication"""
    from app.models.faculty import Faculty
    faculty = Faculty(name="Dr. Unauthorized Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject_data = {
        "name": "Unauthorized Subject",
        "faculty_id": faculty.id,
        "department_id": test_department.id
    }
    response = client.post("/subject/", json=subject_data)
    assert response.status_code == 401

def test_get_subjects(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test getting all subjects"""
    
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. List Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="List Test Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    
    response = client.get("/subject/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(s["name"] == "List Test Subject" for s in data)

def test_get_subject_by_id(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test getting subject by ID"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. ID Test Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="ID Test Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    response = client.get(f"/subject/{subject.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == subject.id
    assert data["name"] == "ID Test Subject"

def test_get_subject_not_found(client: TestClient, auth_headers: dict):
    """Test getting non-existent subject"""
    response = client.get("/subject/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Subject not found" in response.json()["detail"]

def test_update_subject(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test updating subject"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. Update Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="Original Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    update_data = {
        "name": "Updated Subject",
        "faculty_id": faculty.id,
        "department_id": test_department.id
    }
    response = client.put(f"/subject/{subject.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Subject"
    assert data["id"] == subject.id

# def test_update_subject_partial(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
#     """Test partial update of subject"""
#     from app.models.faculty import Faculty
#     from app.models.subject import Subject
#     faculty = Faculty(name="Dr. Partial Professor", department_id=test_department.id)
#     session.add(faculty)
#     session.commit()
#     session.refresh(faculty)
    
#     subject = Subject(name="Partial Test Subject", faculty_id=faculty.id, department_id=test_department.id)
#     session.add(subject)
#     session.commit()
#     session.refresh(subject)
    
#     update_data = {
#         "name": "Partially Updated Subject"
#         # professor_id and department_id not provided, should remain unchanged
#     }
#     response = client.put(f"/subject/{subject.id}", json=update_data, headers=auth_headers)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Partially Updated Subject"
#     assert data["professor_id"] == faculty.id  # Should remain unchanged
#     assert data["department_id"] == test_department.id  # Should remain unchanged

def test_update_subject_invalid_faculty(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test updating subject with invalid faculty"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. Invalid Test Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="Invalid Test Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    update_data = {
        "name": "Updated Subject",
        "professor_id": 999,  # Non-existent faculty
        "department_id": test_department.id
    }
    response = client.put(f"/subject/{subject.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Faculty not found" in response.json()["detail"]

def test_update_subject_invalid_department(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test updating subject with invalid department"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. Invalid Dept Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="Invalid Dept Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    update_data = {
        "name": "Updated Subject",
        "professor_id": faculty.id,
        "department_id": 999  # Non-existent department
    }
    response = client.put(f"/subject/{subject.id}", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_update_subject_not_found(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test updating non-existent subject"""
    from app.models.faculty import Faculty
    faculty = Faculty(name="Dr. Non-existent Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    update_data = {
        "name": "Non-existent Subject",
        "faculty_id": faculty.id,
        "department_id": test_department.id
    }
    response = client.put("/subject/999", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Subject not found" in response.json()["detail"]

def test_delete_subject(client: TestClient, auth_headers: dict, session: Session, test_department: Department):
    """Test deleting subject"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. Delete Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="To Be Deleted Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    response = client.delete(f"/subject/{subject.id}", headers=auth_headers)
    assert response.status_code == 200
    data= response.json()
    assert data["message"] == "Subject deleted successfully"
    assert data["data"]["id"] == subject.id
    
    # Verify subject is deleted
    response = client.get(f"/subject/{subject.id}", headers=auth_headers)
    assert response.status_code == 404

def test_delete_subject_not_found(client: TestClient, auth_headers: dict):
    """Test deleting non-existent subject"""
    response = client.delete("/subject/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Subject not found" in response.json()["detail"]

def test_subject_unauthorized_access(client: TestClient, session: Session, test_department: Department):
    """Test accessing subject endpoints without authentication"""
    from app.models.faculty import Faculty
    from app.models.subject import Subject
    faculty = Faculty(name="Dr. Unauthorized Professor", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)
    
    subject = Subject(name="Unauthorized Subject", faculty_id=faculty.id, department_id=test_department.id)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    
    # Test GET without auth
    response = client.get("/subject/")
    assert response.status_code == 401
    
    # Test GET by ID without auth
    response = client.get(f"/subject/{subject.id}")
    assert response.status_code == 401
    
    # Test PUT without auth
    response = client.put(f"/subject/{subject.id}", json={"name": "Updated"})
    assert response.status_code == 401
    
    # Test DELETE without auth
    response = client.delete(f"/subject/{subject.id}")
    assert response.status_code == 401
