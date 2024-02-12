from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('census-fields', views.census_fields, name='census_fields'),
]
