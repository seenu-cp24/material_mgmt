from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'created_by', 'created_at')
