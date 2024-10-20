from django.contrib import admin
from django.urls import path
from keac.views import http_index

urlpatterns = [
    path('',http_index),
]