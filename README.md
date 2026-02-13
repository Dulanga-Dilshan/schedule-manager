# Schedule Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Deployment](https://img.shields.io/badge/Deployment-Test_Project-lightgrey)
![Server](https://img.shields.io/badge/Server-18.142.252.108-orange)

A minimal Django web application built **specifically as a deployment
test project** to validate production configuration, environment
management, and PostgreSQL integration.

This is not a feature-heavy production system. It is intentionally
simple and focused on verifying correct deployment practices.

------------------------------------------------------------------------

## Live Application

Live URL: http://18.142.252.108/

The application is deployed on a remote Linux server using PostgreSQL to
validate:

-   Environment variable configuration
-   Production settings separation
-   Database migration handling
-   Remote server deployment workflow

------------------------------------------------------------------------

## Core Features

-   User registration & authentication
-   Create, edit, delete schedules
-   Priority levels (High / Medium / Low)
-   User-specific schedule isolation

------------------------------------------------------------------------

## Technical Stack

-   Backend: Python, Django
-   Database: PostgreSQL
-   Frontend: HTML, CSS
-   Deployment: Linux-based remote server

------------------------------------------------------------------------

## Local Installation

``` bash
git clone https://github.com/Dulanga-Dilshan/schedule-manager.git
cd schedule-manager

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

------------------------------------------------------------------------

## Environment Configuration (.env)

This project uses environment variables for sensitive configuration.

Example `.env` file:

``` env
# Django Core
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=18.142.252.108,127.0.0.1,localhost

# Database Configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

After configuring the database:

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

------------------------------------------------------------------------

## Project Purpose

This project exists to validate:

-   Proper Django production settings
-   PostgreSQL integration
-   Secure environment variable usage
-   Remote deployment workflow
-   Basic CRUD architecture in a deployed environment

It serves as a controlled deployment verification project rather than a
feature-rich application.

------------------------------------------------------------------------

## Possible Extensions (Not Implemented)

-   Due dates & reminders
-   Filtering & sorting
-   REST API layer (DRF)
-   Docker containerization
-   CI/CD pipeline integration

------------------------------------------------------------------------

## Author

Developed as a backend deployment validation test project to demonstrate
Django production readiness and PostgreSQL configuration.
