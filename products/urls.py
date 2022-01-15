from django.urls import path
from . import api

urlpatterns = [
    path("products/", api.products),
]
