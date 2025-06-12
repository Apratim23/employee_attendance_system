# 🧑‍💼 Employee Management System (Django + PostgreSQL)

A full-featured backend system to manage employees, attendance, and departmental insights. Built with Django REST Framework, PostgreSQL, Swagger, Token Authentication, and Chart.js visualizations.

---

## 🚀 Features

- Employee CRUD with pagination, filtering, sorting
- Attendance tracking system
- Token-based Authentication (DRF TokenAuth)
- Swagger UI for API exploration
- Visual Charts:
  - 📊 Employees per Department (Pie Chart)
  - 📈 Monthly Attendance Overview (Bar Chart)
- Admin Dashboard + Custom homepage
- Render-compatible deployment (No Docker)

---

## 📁 Folder Structure
```
employee_project/
├── employee_project/ # Django project settings
├── employees/ # App for employee models, views, serializers
├── attendance/ # App for attendance
├── templates/ # HTML templates (charts, homepage)
├── requirements.txt # Python dependencies
├── .env # Example environment file
└── README.md
```

---

## 🔐 Authentication
---
**Endpoint**: `/api-token-auth/`
**Method**: `POST`
**Body**:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
Returns:
```json
{
  "token": "your-auth-token"
}
```
Use this token in Postman or headers:
Authorization: Token your-auth-token
---
📊 Charts Available
---
/charts/ – View:

Employees by department

Monthly attendance bar graph
---
🔧 Local Setup
---
```bash
git clone https://github.com/YOUR_USERNAME/employee-management-system.git
cd employee-management-system
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env  # set your DB credentials
python manage.py migrate
python manage.py seed_data  # optional: add 50 test employees
python manage.py runserver
```
Open http://127.0.0.1:8000/ for homepage.
---
🧪 API Documentation (Swagger)
---
Visit http://127.0.0.1:8000/swagger/
All endpoints with schema, auth, and testable buttons.
---
🚀 Tech Stack Used
---
Backend Framework: Django · Django REST Framework

Database: PostgreSQL

Authentication: Token-Based Auth (DRF AuthToken)

API Docs: Swagger (drf-yasg)

Data Visualization: Chart.js (Pie + Bar Charts via templates)

Deployment: Render (Free Tier)

Extras: Pagination, Filtering, Custom Management Commands for Seeding
