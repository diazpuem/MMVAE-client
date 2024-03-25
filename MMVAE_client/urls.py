from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api', include('api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("index/", views.index),
]
