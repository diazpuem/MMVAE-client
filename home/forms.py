from django import forms
from django.forms  import ModelForm
from .models import RequestFilters, APIRequestInput
from django.core import serializers

#File entry for Database in admin
class GetAPIRequestData(ModelForm):
    class Meta:
        model = APIRequestInput
        fields = ['csv', 'npz']
        # widgets={
        #     'csv': forms.FileField(attrs={'class': 'form-control'}),
        #     #'npz': forms.FileField(attrs={'class': 'form-control'}),
        # }
        
class RequestFiltersForm(ModelForm):
    class Meta:
        model = RequestFilters
        fields = '__all__'
        widgets = {
            'organ_type': forms.Select(attrs={'class': 'form-control'}),
            'tissue': forms.Select(attrs={'class': 'form-control'}),
        }