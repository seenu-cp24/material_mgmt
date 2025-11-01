from django.urls import path
from . import views

urlpatterns = [
    # 🔐 Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # 🏠 Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # 👤 User management (Admin only)
    path('add_user/', views.add_user, name='add_user'),

    # 🔑 Forgot password (Admin reset only)
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
