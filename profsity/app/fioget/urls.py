from django.urls import path
from .views import pager

urlpatterns = [
    path('', pager)
]
