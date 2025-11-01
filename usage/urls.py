from django.urls import path
from . import views

urlpatterns = [
    path('', views.usage_list, name='usage_list'),
    path('add/', views.add_usage, name='add_usage'),
]
