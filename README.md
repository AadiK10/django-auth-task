# Django Authentication System (JWT + Google OAuth)

This project implements a robust user authentication system using Django and Django REST Framework. It features JWT-based authentication, Google OAuth 2.0 integration, a protected dashboard API, and a utility for bulk user insertion.

---

## 🚀 Features

- **User Registration & Login:** Fully integrated JWT (Simple JWT) flow.
- **Google OAuth 2.0:** Social sign-in capabilities via `django-allauth`.
- **Protected Dashboard:** Restricted API access ensuring only authorized users can view data.
- **Bulk Data Handling:** High-performance insertion of 10,000 users using Django ORM.
- **Environment Security:** Secure management of secrets and keys using `.env` files.

---

## 🛠 Tech Stack

- **Framework:** Django & Django REST Framework
- **Authentication:** django-allauth, dj-rest-auth, Simple JWT
- **Database:** SQLite (Default for development)
- **Language:** Python 3.x

---

## ⚙️ Setup Instructions (Local)

### 1. Project Initialization
```bash
# Clone the repository
git clone <repository-url>
cd django-auth-task

# Create & activate virtual environment
# Windows:
python -m venv venv
venv\Scripts\activate

# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
2. Environment Variables & SecurityCreate a .env file in the project root. This file is ignored by Git to prevent security leaks.Code snippetDJANGO_SECRET_KEY=your-django-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
3. Database Setup & RunBash# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver
The application will be live at: http://127.0.0.1:8000/

🔑 API EndpointsActionEndpointRegister/api/auth/registration/Login/api/auth/login/Logout/api/auth/logout/Dashboard/api/dashboard/Google Login/accounts/google/login/

📊 Bulk User InsertionThis project includes a script to insert 10,000 users efficiently. It utilizes the Django ORM bulk_create method to minimize database hits and includes validation logic to prevent duplicate entries.

👤Author
Aaditya Kini