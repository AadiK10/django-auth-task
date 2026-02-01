from django.urls import path
from .views import (
    dashboard, bulk_create_users, login_page, dashboard_ui, signup_page, logout_ui
)

urlpatterns = [
    path('', signup_page),              
    path('login/', login_page),
    path('signup/', signup_page),
    path('logout-ui/', logout_ui),      
    path('dashboard/', dashboard),
    path('dashboard-ui/', dashboard_ui),
    path('bulk-insert-users/', bulk_create_users),  
]
