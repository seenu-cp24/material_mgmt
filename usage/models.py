from django.db import models
from django.contrib.auth.models import User
from materials.models import Material

class MaterialUsage(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100, blank=True, null=True)
    quantity_used = models.PositiveIntegerField()
    issued_to = models.CharField(max_length=100, blank=True, null=True)
    issue_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.material.name} - {self.unit} - {self.quantity_used}"
