from django.contrib import admin
from django.urls import path
from keac.views import *

urlpatterns = [
    path('',http_index)
]