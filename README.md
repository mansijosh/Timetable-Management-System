# 🗓️ Timetable Management System (Backend + Frontend)

A smart and automated **Timetable Management System** for engineering colleges, built using **FastAPI** for backend, **React** for frontend, and **PostgreSQL** for managing complex scheduling data.

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

### 💻 Frontend (React)
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
| Frontend    | **Svelt**,  
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

2. Open Adminer in your browser:
    ```bash
    http://localhost:8080

3. Log in using the following credentials (match with your .env file):

    System: PostgreSQL
    Server: db
    Username: <your_postgres_user>
    Password: <your_postgres_password>
    Database: <your_database_name>