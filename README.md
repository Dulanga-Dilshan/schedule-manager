# Schedule Manager

A minimal Django web application that allows users to manage personal
schedules.

This project was built as a deployment test application and demonstrates
basic authentication and CRUD functionality using Django.

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
-   SQLite (default)
-   Gunicorn (for production)
-   Nginx (reverse proxy in deployment)

------------------------------------------------------------------------

## Local Development Setup

### 1. Clone the repository

``` bash
git clone <your-repo-url>
cd schedule_manager
```

### 2. Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# or
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Create `.env` file in project root

    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

### 5. Run migrations

``` bash
python manage.py migrate
```

### 6. Start development server

``` bash
python manage.py runserver
```

------------------------------------------------------------------------

## Production Deployment (Example)

1.  Set environment variables properly.
2.  Run:

``` bash
python manage.py migrate
python manage.py collectstatic --noinput
```

3.  Start with Gunicorn:

``` bash
gunicorn schedule_manager.wsgi:application
```

4.  Configure Nginx to reverse proxy to Gunicorn.

------------------------------------------------------------------------

## Environment Variables

  Variable               Description
  ---------------------- ---------------------------
  DJANGO_SECRET_KEY      Django secret key
  DJANGO_DEBUG           True/False
  DJANGO_ALLOWED_HOSTS   Comma-separated host list

------------------------------------------------------------------------

## Purpose

This project was created to test production deployment workflows
including:

-   Environment variable management
-   Gunicorn configuration
-   Nginx reverse proxy setup
-   EC2 server configuration
