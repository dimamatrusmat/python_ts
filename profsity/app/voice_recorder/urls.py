from django.urls import path
from .views import record, index, record_detail

urlpatterns = [
    path("", index, name="index"),
    path("record/", record, name="record"),
    path("record/detail/<uuid:id>/", record_detail, name="record_detail"),
]
