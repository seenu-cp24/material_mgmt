from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to login page
def redirect_to_login(request):
    return redirect('accounts:login')  # use accounts namespace

urlpatterns = [
    path('', redirect_to_login),  # redirect home → login
    path('admin/', admin.site.urls),

    # Apps with namespaces
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('materials/', include(('materials.urls', 'materials'), namespace='materials')),
    path('reports/', include(('reports.urls', 'reports'), namespace='reports')),
    path('usage/', include(('usage.urls', 'usage'), namespace='usage')),
]
