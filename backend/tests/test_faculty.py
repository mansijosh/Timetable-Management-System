from fastapi.testclient import TestClient
from sqlmodel import Session
from app.models.department import Department
from app.models.faculty import Faculty


def test_create_faculty(
    client: TestClient, auth_headers: dict, test_department: Department
):
    """Test creating a new faculty"""
    faculty_data = {"name": "Dr. John Smith", "department_id": test_department.id}
    response = client.post("/faculty/", json=faculty_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Dr. John Smith"
    assert data["department"]["id"] == test_department.id
    assert "id" in data


def test_create_faculty_invalid_department(client: TestClient, auth_headers: dict):
    """Test creating faculty with non-existent department"""
    faculty_data = {"name": "Dr. Jane Doe", "department_id": 999}
    response = client.post("/faculty/", json=faculty_data, headers=auth_headers)
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_create_faculty_unauthorized(client: TestClient, test_department: Department):
    """Test creating faculty without authentication"""
    faculty_data = {"name": "Dr. Bob Wilson", "department_id": test_department.id}
    response = client.post("/faculty/", json=faculty_data)
    assert response.status_code == 401


def test_get_faculties(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test getting all faculties"""

    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Alice Johnson", department_id=test_department.id)
    session.add(faculty)
    session.commit()

    response = client.get("/faculty/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(f["name"] == "Dr. Alice Johnson" for f in data)


def test_get_faculty_by_id(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test getting faculty by ID"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Bob Brown", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    response = client.get(f"/faculty/{faculty.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == faculty.id
    assert data["name"] == "Dr. Bob Brown"


def test_get_faculty_not_found(client: TestClient, auth_headers: dict):
    """Test getting non-existent faculty"""
    response = client.get("/faculty/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Faculty not found" in response.json()["detail"]


def test_update_faculty(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test updating faculty"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Original Name", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    update_data = {"name": "Dr. Updated Name", "department_id": test_department.id}
    response = client.put(
        f"/faculty/{faculty.id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Dr. Updated Name"
    assert data["id"] == faculty.id


def test_update_faculty_partial(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test partial update of faculty"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Partial Test", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    update_data = {"name": "Dr. Partially Updated", "department_id": test_department.id}
    response = client.put(
        f"/faculty/{faculty.id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Dr. Partially Updated"
    assert data["department"]["id"] == test_department.id


def test_update_faculty_invalid_department(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test updating faculty with invalid department"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Test Faculty", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    update_data = {
        "name": "Dr. Updated Faculty",
        "department_id": 999,  # Non-existent department
    }
    response = client.put(
        f"/faculty/{faculty.id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 404
    assert "Department not found" in response.json()["detail"]


def test_update_faculty_not_found(
    client: TestClient, auth_headers: dict, test_department: Department
):
    """Test updating non-existent faculty"""
    update_data = {"name": "Dr. Non-existent", "department_id": test_department.id}
    response = client.put("/faculty/999", json=update_data, headers=auth_headers)
    assert response.status_code == 404
    assert "Faculty not found" in response.json()["detail"]


def test_delete_faculty(
    client: TestClient,
    auth_headers: dict,
    session: Session,
    test_department: Department,
):
    """Test deleting faculty"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. To Be Deleted", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    response = client.delete(f"/faculty/{faculty.id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Faculty deleted successfully"
    assert data["data"]["id"] == faculty.id

    response = client.get(f"/faculty/{faculty.id}", headers=auth_headers)
    assert response.status_code == 404


def test_delete_faculty_not_found(client: TestClient, auth_headers: dict):
    """Test deleting non-existent faculty"""
    response = client.delete("/faculty/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Faculty not found" in response.json()["detail"]


def test_faculty_unauthorized_access(
    client: TestClient, session: Session, test_department: Department
):
    """Test accessing faculty endpoints without authentication"""
    from app.models.faculty import Faculty

    faculty = Faculty(name="Dr. Unauthorized Test", department_id=test_department.id)
    session.add(faculty)
    session.commit()
    session.refresh(faculty)

    response = client.get("/faculty/")
    assert response.status_code == 401

    response = client.get(f"/faculty/{faculty.id}")
    assert response.status_code == 401

    response = client.put(f"/faculty/{faculty.id}", json={"name": "Updated"})
    assert response.status_code == 401

    response = client.delete(f"/faculty/{faculty.id}")
    assert response.status_code == 401
