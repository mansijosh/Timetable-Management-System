# Testing Guide

This directory contains comprehensive test cases for the Timetable Management System API.

## Test Database Configuration

### For PostgreSQL Testing (Recommended)

1. **Create a test database:**
   ```sql
   CREATE DATABASE timetable_test_db;
   ```

2. **Set environment variable:**
   ```bash
   export TEST_DATABASE_URL=postgresql://username:password@localhost:5432/timetable_test_db
   ```

3. **Run tests:**
   ```bash
   pytest
   ```

### For SQLite Testing (Fallback/CI)

If PostgreSQL is not available, tests will automatically fall back to in-memory SQLite:

```bash
# No environment variable needed - will use SQLite automatically
pytest
```

## Test Structure

- `conftest.py` - Test configuration and fixtures
- `test_auth.py` - Authentication API tests
- `test_department.py` - Department CRUD tests
- `test_classroom.py` - Classroom CRUD tests
- `test_faculty.py` - Faculty CRUD tests
- `test_subject.py` - Subject CRUD tests

## Running Tests

### All Tests
```bash
pytest
```

### Specific Test Files
```bash
pytest tests/test_auth.py
pytest tests/test_department.py
```

### With Coverage
```bash
pytest --cov=app
pytest --cov=app --cov-report=html
```

### Verbose Output
```bash
pytest -v
```

## Test Features

- **Database Isolation**: Each test runs in a transaction that gets rolled back
- **Authentication**: Mock JWT tokens for testing protected endpoints
- **Fixtures**: Pre-configured test data for consistent testing
- **PostgreSQL Support**: Uses the same database as production
- **Comprehensive Coverage**: All CRUD operations, validation, and error scenarios
