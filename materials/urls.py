from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    # Materials CRUD
    path('', views.material_list, name='material_list'),
    path('add/', views.add_material, name='add_material'),
    path('edit/<int:material_id>/', views.edit_material, name='edit_material'),
    path('delete/<int:material_id>/', views.delete_material, name='delete_material'),

    # Reports Dashboard
    path('reports/', views.report_list, name='report_list'),

    # Individual Reports
    path('reports/stock-summary/', views.stock_summary, name='stock_summary'),
    path('reports/low-stock/', views.low_stock_report, name='low_stock_report'),
    path('reports/date-wise/', views.date_wise_report, name='date_wise_report'),
]
