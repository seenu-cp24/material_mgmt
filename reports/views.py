from django.shortcuts import render
from django.http import HttpResponse
from materials.models import Material
import csv

def unit_wise_report(request):
    # Aggregate materials by unit
    units = {}
    materials = Material.objects.all()
    for m in materials:
        units[m.unit] = units.get(m.unit, 0) + m.quantity

    return render(request, 'reports/unit_report.html', {'units': units})


def download_csv(request):
    # Generate CSV file
    materials = Material.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="materials_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description', 'Quantity', 'Unit', 'Created By'])
    for m in materials:
        writer.writerow([m.name, m.description, m.quantity, m.unit, m.created_by.username])

    return response
