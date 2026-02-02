# Django Authentication System (JWT + Google OAuth)

This project implements a secure user authentication system using **Django** and **Django REST Framework**.  
It supports standard authentication, JWT-based login/logout, Google OAuth 2.0 sign-in, a protected dashboard API, and bulk user insertion.

---

## Features

- User Registration (username/email & password)
- Login & Logout using JWT (Simple JWT)
- Google OAuth 2.0 Authentication
- Protected Dashboard API
- Bulk insertion of 10,000 users using Django ORM
- Secure handling of secrets using environment variables

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- django-allauth
- dj-rest-auth
- Simple JWT
- SQLite (local development)

---

## Project Setup (Local)

### 1. Clone the repository
```bash
git clone <repository-url>
cd django-auth-task
```

### 2. Create and activate virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-django-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

> The `.env` file is ignored by Git and **must not be committed**.

---

## Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Run the Server
```bash
python manage.py runserver
```

Server runs at:
```
http://127.0.0.1:8000/
```

---

## API Endpoints

| Action     | Endpoint                   |
|-----------|----------------------------|
| Sign Up   | /api/auth/registration/    |
| Login     | /api/auth/login/           |
| Logout    | /api/auth/logout/          |
| Dashboard | /api/dashboard/            |

---

## Google OAuth Login

Visit:
```
http://127.0.0.1:8000/accounts/google/login/
```

Authenticate with Google → user is redirected to dashboard.

---

## Bulk User Insertion

- Inserts **10,000 users** in a single execution
- Uses `bulk_create` for high performance
- Includes basic duplicate validation

---

## Security Notes

- Secrets are stored using environment variables
- `.env` file is excluded from version control
- JWT and session authentication handled securely

---

## Author

**Aaditya Kini**
