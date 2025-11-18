from django.urls import path
from . import views

app_name = 'usage'  # <- This registers the namespace

urlpatterns = [
    path('', views.usage_list, name='usage_list'),
    path('add/', views.add_usage, name='add_usage'),
]
