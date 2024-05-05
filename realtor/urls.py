from django.urls import path
from . import views

urlpatterns = [
    path("", views.realtor, name="realtor"),
    path("create_property/", views.create_property, name="create_property"),
]