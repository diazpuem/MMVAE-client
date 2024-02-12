from django.shortcuts import render
from .api import census

def index(request):
    return render(request, 'index.html')

def census_fields(request):
    fields = census.fetchFilteringFields()
    return render(request, 'census_fields.html', {'fields': fields})