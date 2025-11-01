from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material

@login_required
def material_list(request):
    materials = Material.objects.all().order_by('-created_at')
    return render(request, 'materials/material_list.html', {'materials': materials})

@login_required
def add_material(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        created_by = request.user

        Material.objects.create(
            name=name,
            description=description,
            quantity=quantity,
            unit=unit,
            created_by=created_by
        )
        return redirect('material_list')

    return render(request, 'materials/add_material.html')

@login_required
def edit_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)

    if request.method == 'POST':
        material.name = request.POST.get('name')
        material.description = request.POST.get('description')
        material.quantity = request.POST.get('quantity')
        material.unit = request.POST.get('unit')
        material.save()
        return redirect('material_list')

    return render(request, 'materials/edit_material.html', {'material': material})

@login_required
def delete_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    material.delete()
    return redirect('material_list')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def report_list(request):
    return render(request, 'materials/report_list.html')
