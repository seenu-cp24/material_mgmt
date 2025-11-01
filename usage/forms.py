from django import forms
from .models import MaterialUsage

class MaterialUsageForm(forms.ModelForm):
    class Meta:
        model = MaterialUsage
        fields = ['material', 'unit', 'quantity_used', 'issued_to']
        widgets = {
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_used': forms.NumberInput(attrs={'class': 'form-control'}),
            'issued_to': forms.TextInput(attrs={'class': 'form-control'}),
        }
