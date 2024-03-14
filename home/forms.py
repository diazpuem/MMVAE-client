from django import forms
from django.forms  import ModelForm
from .models import RequestFilters


class RequestFiltersForm(ModelForm):
    class Meta:
        model = RequestFilters
        fields = '__all__'
        widgets = {
            'organ_type': forms.Select(attrs={'class': 'form-control'}),
            'tissue': forms.Select(attrs={'class': 'form-control'}),
            'csv': forms.FileField(attrs={'class': 'form-control'}),
        }