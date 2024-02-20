from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('graphs', views.graphs, name='graphs'),
]
