import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models.subject import Subject
from app.models.faculty import Faculty
from app.models.classroom import Classroom
from app.models.department import Department


def test_get_dashboard_stats(
    client: TestClient,
    auth_headers: dict,
    session: Session
):
    """Test dashboard statistics endpoint"""

    department = Department(name="Computer Science", year=2024)
    session.add(department)
    session.commit()
    session.refresh(department)

    faculty1 = Faculty(name="Dr. A", department_id=department.id)
    faculty2 = Faculty(name="Dr. B", department_id=department.id)
    session.add_all([faculty1, faculty2])
    session.commit()
    session.refresh(faculty1)
    session.refresh(faculty2)

    subject1 = Subject(
        name="Maths",
        faculty_id=faculty1.id,
        department_id=department.id
    )
    subject2 = Subject(
        name="Physics",
        faculty_id=faculty2.id,
        department_id=department.id
    )
    session.add_all([subject1, subject2])
    session.commit()

    classroom1 = Classroom(
        building_name="Block A",
        room_no="101",
        capacity=50,
        department_id=department.id
    )
    classroom2 = Classroom(
        building_name="Block B",
        room_no="202",
        capacity=60,
        department_id=department.id
    )
    session.add_all([classroom1, classroom2])
    session.commit()

    response = client.get("/dashboard/stats", headers=auth_headers)

    assert response.status_code == 200

    data = response.json()

    assert data["total_departments"] == 1
    assert data["total_faculties"] == 2
    assert data["total_subjects"] == 2
    assert data["total_classrooms"] == 2
