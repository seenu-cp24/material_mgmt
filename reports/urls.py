from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_wise_report, name='unit_report'),
    path('download/', views.download_csv, name='download_csv'),
]
