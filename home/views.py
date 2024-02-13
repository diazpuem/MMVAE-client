from django.shortcuts import render
from .api import census

def index(request):
    return render(request, 'index.html')

# def graphs(request):
    
