# 🗓️ Timetable Management System (Backend + Frontend)

A smart and automated **Timetable Management System** for engineering colleges, built using **FastAPI** for backend, **Svelte** for frontend, and **PostgreSQL** for managing complex scheduling data.

---

## 🎯 Purpose

In most engineering colleges, preparing a timetable is a **time-consuming and error-prone** process.

Common issues include:
- Teachers being double-booked
- Classroom overlaps
- Unbalanced workloads
- Inefficient resource utilization

> 🎯 Our system aims to **automate and optimize** the timetable generation process using a smart algorithm and AI-powered suggestions.

---

## 💡 Key Features

### 🔧 Backend (FastAPI)
- Teacher, Department, Subject, and Classroom management
- Conflict detection & auto-suggestions
- Real-time alerts for leave, conflicts, and schedule changes
- Downloadable PDF timetables
- Teacher and room utilization reports
- Admin dashboard APIs
- Secure role-based access (Admin, Faculty)

### 💻 Frontend (Svelte)
- Clean, user-friendly dashboard for Admin and Faculty
- Drag-and-drop timetable editor
- Real-time views of schedule
- PDF preview and download
- Report and analytics views
- Notifications and alerts interface

---

## 🧱 Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Frontend    | **Svelte** |
| Backend     | **FastAPI** (Python) |
| Database    | **PostgreSQL** (Recommended) |
| Containerization | **Docker**, Docker Compose |
| Scheduling Logic | Custom Python logic
| PDF Reports | **ReportLab** |
| Deployment  |  Render / VPS with Docker |


## Database Design Link

https://lucid.app/lucidchart/58446467-6884-4005-a6b8-872b6a062e01/edit?viewport_loc=-1079%2C-454%2C3561%2C1327%2C0_0&invitationId=inv_9f8ddd78-eeca-4e1b-9255-cff3a49316b0


##  ⚙️Project architecture section

<img src="./TimetableDatabaseDesign.jpg"/>



# 🛠️ Database Management with Adminer

This project uses **[Adminer](https://www.adminer.org/)** as a lightweight web-based database management tool for PostgreSQL.  
Adminer provides an easy-to-use UI to browse tables, run queries, and manage the database directly from your browser.

---

1. Start all services:
   ```bash
   docker-compose up --build
# Stop containers
docker-compose down

# Rebuild and start in detached mode
docker-compose up --build -d

# Or rebuild just the backend service
docker-compose build backend
docker-compose up -d
2. Open Adminer in your browser:
    ```bash
    http://localhost:8080

3. Log in using the following credentials (match with your .env file):

    System: PostgreSQL
    Server: db
    Username: <your_postgres_user>
    Password: <your_postgres_password>
    Database: <your_database_name>


##  🛠️ Command to Copy .env.example to .env

#### Copy the example environment file and rename it to .env:

1. For Linux / macOS / Git Bash:
   ```bash
   cp .env.example .env


2. For Windows (Command Prompt):
   ```bash
   copy .env.example .env


3. For Windows (PowerShell):
   ```bash
   Copy-Item .env.example .env

Then, open the .env file and replace the dummy values with actual credentials 

---

## 🧪 Testing

The project includes comprehensive test coverage using **pytest** for all API endpoints.

### Prerequisites for Testing

Make sure you have the test dependencies installed:

```bash
pip install -r requirements.txt
```

### Running Tests

#### Run All Tests
```bash
# From the backend directory
cd backend
pytest

# With verbose output
pytest -v

# With coverage report
pytest --cov=app
```

#### Run Specific Test Files
```bash
# Test authentication APIs
pytest tests/test_auth.py

# Test department APIs
pytest tests/test_department.py

# Test classroom APIs
pytest tests/test_classroom.py

# Test faculty APIs
pytest tests/test_faculty.py

# Test subject APIs
pytest tests/test_subject.py
```

#### Run Specific Test Functions
```bash
# Run a specific test function
pytest tests/test_auth.py::test_register_user

# Run tests matching a pattern
pytest -k "test_create"
```

### Test Database Configuration

The tests use **PostgreSQL** (same as production) with the following setup:
- **Test Database**: Uses the same PostgreSQL instance as development
- **Isolation**: Each test runs in a transaction that gets rolled back
- **Fixtures**: Pre-configured test data for consistent testing
- **Authentication**: Mock JWT tokens for testing protected endpoints

### Test Coverage

The test suite covers:
- ✅ **Authentication**: Registration, login, password handling
- ✅ **CRUD Operations**: Create, Read, Update, Delete for all entities
- ✅ **Authorization**: Protected endpoint access
- ✅ **Validation**: Input validation and error handling
- ✅ **Relationships**: Foreign key constraints and data integrity
- ✅ **Edge Cases**: Not found scenarios, duplicates, invalid data

### Test Structure

```
backend/
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration and fixtures
│   ├── test_auth.py         # Authentication tests
│   ├── test_department.py   # Department API tests
│   ├── test_classroom.py    # Classroom API tests
│   ├── test_faculty.py      # Faculty API tests
│   └── test_subject.py      # Subject API tests
└── pytest.ini              # Pytest configuration
```

### Environment Variables for Testing

Ensure your `.env` file contains the PostgreSQL connection details:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/timetable_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Continuous Integration

For CI/CD pipelines, you can run tests with:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=app --cov-report=xml

# Generate HTML coverage report
pytest --cov=app --cov-report=html
```