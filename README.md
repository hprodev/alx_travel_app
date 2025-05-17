# ALX Travel App

A robust Django-based travel listing platform that allows users to explore and share travel destinations.

## Project Overview

ALX Travel App is a full-featured web application built with Django and Django REST Framework, designed to serve as a foundation for a travel listing platform. The platform includes API documentation, database integration, and a modern architecture to support travel listing management.

## Features

- RESTful API for managing travel listings
- MySQL database integration
- Comprehensive API documentation with Swagger/ReDoc
- CORS support for frontend integration
- Admin interface for content management
- Environment-based configuration

## Technology Stack

- **Backend**: Django 5.2.1, Django REST Framework
- **Database**: MySQL
- **Documentation**: drf-yasg (Swagger/ReDoc)
- **Development**: django-environ for environment variable management
- **Security**: CORS headers configuration
- **Task Management**: Celery (configured for future implementation)

## Prerequisites

- Python 3.x
- MySQL Server
- Git

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```

2. **Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows (Git Bash)
source env/Scripts/activate

# macOS/Linux
source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root directory with the following variables:

```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

5. **Create MySQL database**

```bash
mysql -u root -p
```

When prompted, enter your MySQL root password, then:

```sql
CREATE DATABASE alx_travel_db;
EXIT;
```

6. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create a superuser**

```bash
python manage.py createsuperuser
```

8. **Run the development server**

```bash
python manage.py runserver
```

## Project Structure

```
alx_travel_app/
├── alx_travel_app/         # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings and configurations
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py
├── listings/               # Listings application
│   ├── __init__.py
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── tests.py            # Application tests
│   ├── urls.py             # Listings URL configuration
│   └── views.py            # API views
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── LICENSE                 # Project license
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/listings/` | GET | List all travel listings |
| `/api/listings/` | POST | Create a new listing |
| `/api/listings/{id}/` | GET | Retrieve a specific listing |
| `/api/listings/{id}/` | PUT/PATCH | Update a listing |
| `/api/listings/{id}/` | DELETE | Delete a listing |

## Documentation

API documentation is available at the following endpoints:

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Admin Interface

Access the admin interface at `/admin/` to manage listings and users.
