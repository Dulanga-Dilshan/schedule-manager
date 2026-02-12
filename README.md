# Schedule Manager

A minimal Django web application that allows users to manage personal
schedules.

This project was built as a deployment and database configuration test
application. It demonstrates authentication, CRUD operations, and
PostgreSQL integration using Django.

------------------------------------------------------------------------

## Features

-   User registration
-   User login/logout
-   Create schedules
-   Edit schedules
-   Delete schedules
-   Set schedule priority:
    -   High
    -   Medium
    -   Low

------------------------------------------------------------------------

## Tech Stack

-   Python 3
-   Django
-   PostgreSQL
-   Gunicorn (production server)
-   Nginx (reverse proxy for deployment)

------------------------------------------------------------------------

## Database Configuration (PostgreSQL)

This project uses PostgreSQL as the primary database.

### Required Environment Variables

Create a `.env` file in the project root:

    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

    POSTGRES_DB=schedule_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=yourpassword
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432

### Install PostgreSQL Driver

    pip install psycopg2-binary

### Apply Migrations

    python manage.py migrate

------------------------------------------------------------------------

## Local Development Setup

### 1. Clone Repository

    git clone <your-repo-url>
    cd schedule_manager

### 2. Create Virtual Environment

    python -m venv venv
    venv\Scripts\activate   # Windows

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run Server

    python manage.py runserver

------------------------------------------------------------------------

## Production Deployment Overview

Deployment tested using:

-   Gunicorn
-   Nginx
-   Ubuntu (EC2)

Production steps:

    python manage.py migrate
    python manage.py collectstatic --noinput
    gunicorn schedule_manager.wsgi:application

------------------------------------------------------------------------

## Purpose

This project was created to practice:

-   PostgreSQL integration with Django
-   Environment variable management
-   Production-ready configuration
-   Server deployment using Gunicorn and Nginx
