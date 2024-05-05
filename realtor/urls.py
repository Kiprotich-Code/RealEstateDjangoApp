from django.urls import path
from . import views

urlpatterns = [
    path("", views.realtor, name="realtor"),
    path("create_property/", views.create_property, name="create_property"),

    # cbv 
    path("property_list/", views.PropertyListView.as_view(), name="property_list"),
    path("property_details/<pk>", views.PropertyDetailView.as_view(), name="property_details"),
]