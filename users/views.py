from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.db import IntegrityError

import requests
from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email
    })

@api_view(['POST'])
def bulk_create_users(request):
    users = []
    for i in range(1, 10001):
        users.append(
            User(
                username=f"user{i}",
                email=f"user{i}@test.com"
            )
        )

    try:
        User.objects.bulk_create(users, ignore_conflicts=True)
        return Response({"message": "10,000 users inserted successfully"})
    except IntegrityError:
        return Response({"error": "Error inserting users"}, status=400)
    
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post(
            "http://127.0.0.1:8000/api/auth/login/",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            data = response.json()
            request.session["access"] = data.get("access")
            return redirect("/api/dashboard-ui/")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "auth/login.html")

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        response = requests.post(
            "http://127.0.0.1:8000/api/auth/registration/",
            json={
                "username": username,
                "email": email,
                "password1": password1,
                "password2": password2
            }
        )

        if response.status_code == 201 or response.status_code == 200:
            return redirect("/api/login/")
        else:
            messages.error(request, "Signup failed. Check details.")

    return render(request, "auth/signup.html")


def dashboard_ui(request):
    token = request.session.get("access")
    if not token:
        return redirect("/api/login/")

    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    except AuthenticationFailed:
        return redirect("/api/login/")

    return render(request, "dashboard/dashboard.html", {
        "user": user
    })

def logout_ui(request):
    request.session.flush()   # clears JWT from session
    return redirect("/api/login/")

