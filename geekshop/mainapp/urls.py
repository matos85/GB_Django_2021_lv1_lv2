from django.contrib import admin
from django.urls import path
from .views import index, products, contact

urlpatterns = [
    path('', index),
    path('products/', products),
    path('contact/', contact),
]
