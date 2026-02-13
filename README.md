# Schedule Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Deployment](https://img.shields.io/badge/Deployed-Live-success)
![Server](https://img.shields.io/badge/Server-18.142.252.108-orange)

A production-ready Django web application for managing personal
schedules, built and deployed as part of a backend deployment validation
project.

------------------------------------------------------------------------

## 🌐 Live Application

**Live URL:** http://18.142.252.108/

This application is actively deployed on a remote server to demonstrate
real-world backend deployment capability using PostgreSQL.

------------------------------------------------------------------------

## 🚀 Key Features

-   Secure user registration and authentication
-   Full CRUD functionality for schedules
-   Priority management system (High / Medium / Low)
-   User-specific schedule isolation
-   Clean and minimal UI design
-   Live production deployment

------------------------------------------------------------------------

## 🛠 Technical Stack

-   **Backend:** Python, Django
-   **Database:** PostgreSQL
-   **Frontend:** HTML, CSS
-   **Deployment:** Linux-based remote server

------------------------------------------------------------------------

## 📦 Installation (Local Setup)

``` bash
git clone https://github.com/your-username/schedule-manager.git
cd schedule-manager

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### Configure PostgreSQL

Create a PostgreSQL database and update your `.env` or `settings.py`
with:

``` env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Then run:

``` bash
python manage.py migrate
python manage.py runserver
```

------------------------------------------------------------------------

## 🎯 Project Objectives

This project demonstrates:

-   Django authentication flow implementation
-   PostgreSQL database integration
-   Production-ready database configuration
-   CRUD operations with user-based data access control
-   Environment-based configuration handling
-   Live server deployment

------------------------------------------------------------------------

## 📈 Potential Enhancements

-   Due date tracking and reminders
-   Filtering and sorting by priority
-   REST API integration (Django REST Framework)
-   Docker containerization
-   CI/CD pipeline integration

------------------------------------------------------------------------

## 👨‍💻 Author

Developed as a backend-focused deployment test to validate production
readiness, PostgreSQL integration, and core Django fundamentals.
