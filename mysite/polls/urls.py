from django.contrib import admin
from django.urls import path
from . import models
from .models import Post
from django.db import connection
from .views import create, delete, edit, main, home

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    
]
# i would call these methods and wanted to print it in the console terminal)