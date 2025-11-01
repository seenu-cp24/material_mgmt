from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MaterialUsage
from .forms import MaterialUsageForm

@login_required
def usage_list(request):
    usages = MaterialUsage.objects.all()
    return render(request, 'usage/usage_list.html', {'usages': usages})

@login_required
def add_usage(request):
    if request.method == 'POST':
        form = MaterialUsageForm(request.POST)
        if form.is_valid():
            usage = form.save(commit=False)
            usage.created_by = request.user
            usage.save()
            return redirect('usage_list')
    else:
        form = MaterialUsageForm()
    return render(request, 'usage/add_usage.html', {'form': form})
