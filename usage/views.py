from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # For showing error/success messages
from .models import MaterialUsage
from .forms import MaterialUsageForm
from materials.models import Material  # Import Material to check stock
from django.db.models import Sum

# -------------------------------
# List all usages
# -------------------------------
def usage_list(request):
    usages = MaterialUsage.objects.all().order_by('-issue_date')
    return render(request, 'usage/usage_list.html', {'usages': usages})


# -------------------------------
# Add new usage
# -------------------------------
def add_usage(request):
    if request.method == 'POST':
        form = MaterialUsageForm(request.POST)
        if form.is_valid():
            usage_instance = form.save(commit=False)  # Don't save yet

            # Get the selected material
            material = usage_instance.material
            requested_qty = usage_instance.quantity_used

            # Calculate available quantity
            total_used = MaterialUsage.objects.filter(material=material).aggregate(
                total_used=Sum('quantity_used')
            )['total_used'] or 0
            remaining_qty = material.quantity - total_used

            if requested_qty > remaining_qty:
                # Not enough stock, show error message
                messages.error(request, f"❌ Not enough stock for '{material.name}'. Available: {remaining_qty}, Requested: {requested_qty}")
                return render(request, 'usage/add_usage.html', {'form': form})

            # Enough stock, save usage
            usage_instance.save()
            messages.success(request, f"✅ Material '{material.name}' issued successfully!")
            return redirect('usage:usage_list')
    else:
        form = MaterialUsageForm()

    return render(request, 'usage/add_usage.html', {'form': form})
