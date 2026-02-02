# Django Authentication System (JWT + Google OAuth)

This project implements a complete authentication system using **Django** and **Django REST Framework**.  
It includes JWT-based authentication, Google OAuth 2.0 login, a protected dashboard (API + UI), and bulk user insertion.

---

## 🚀 Features

- User Sign Up (username, email & password)
- Login & Logout using JWT
- Google OAuth 2.0 Sign-In (via django-allauth)
- Protected Dashboard API
- Dashboard UI built using Django Templates
- Bulk insertion of 10,000 users using Django ORM (`bulk_create`)
- Secure handling of secrets using environment variables

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework (DRF)
- django-allauth
- dj-rest-auth
- Simple JWT
- SQLite (local development)

---

## ⚙️ Project Setup (Local)

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd django-auth-task
2️⃣ Create and activate virtual environment
Windows

python -m venv venv
venv\Scripts\activate
macOS / Linux

python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables
Create a .env file in the project root:
DJANGO_SECRET_KEY=your-django-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

🗄 Database Setup
python manage.py migrate
python manage.py createsuperuser

▶️ Run the Server
python manage.py runserver
Server will start at:

http://127.0.0.1:8000/
🔑 Authentication & API Endpoints
Authentication (JWT)
Action	Endpoint
Sign Up (API)	/api/auth/registration/
Login (API)	/api/auth/login/
Logout (API)	/api/auth/logout/
Token Refresh	/api/auth/token/refresh/
UI Pages (Django Templates)
Page	URL
Sign Up (UI)	/api/ or /api/signup/
Login (UI)	/api/login/
Logout (UI)	/api/logout-ui/
Dashboard (UI)	/api/dashboard-ui/
Dashboard API (Protected)
Action	Endpoint
User Dashboard Data	/api/dashboard/
⚠️ Requires authentication (JWT or session)

🔒 Google OAuth Login
Google OAuth is implemented using django-allauth.

Login URL:
http://127.0.0.1:8000/accounts/google/login/

Flow:
User clicks Continue with Google
Google consent screen appears
User approves permissions
User is logged in
Redirected to dashboard

📊 Bulk User Insertion
Endpoint:

POST /api/bulk-insert-users/
Inserts 10,000 users in a single execution
Uses Django ORM bulk_create
Includes basic validation to avoid duplicates
Optimized for performance

🔐 Security Notes
Sensitive credentials are stored using environment variables
.env file is not committed to GitHub
JWT-based authentication used for APIs
Django sessions used for UI authentication
Google OAuth configured securely via Google Cloud Console

✅ Completion Status
✔ User authentication system
✔ JWT-based login & logout
✔ Google OAuth 2.0 integration
✔ Protected dashboard (API + UI)
✔ Bulk user insertion
✔ Secure environment variable handling
✔ Local setup instructions included

👤 Author
Aaditya Kini