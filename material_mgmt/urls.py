from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to login page
def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login),  # redirect home → login
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('materials/', include('materials.urls')),
    path('reports/', include('reports.urls')),
    path('usage/', include('usage.urls')),
]
