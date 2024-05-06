from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.realtor, name="realtor"),
    path("create_property/", views.create_property, name="create_property"),

    # cbv 
    path("property_list/", views.PropertyListView.as_view(), name="property_list"),
    path("property_details/<pk>", views.PropertyDetailView.as_view(), name="property_details"),
    path("update_property/<pk>", views.PropertyUpdateView.as_view(), name="update_property"),

    #sphaghetti
    path('orders/', TemplateView.as_view(template_name="realtors/orders.html"), name="orders"),
    path('callbacks/', TemplateView.as_view(template_name="realtors/callbacks.html"), name="callbacks"),
    path('messages/', TemplateView.as_view(template_name="realtors/messages.html"), name="messages"),
    path('analytics/', TemplateView.as_view(template_name="realtors/analytics.html"), name="analytics"),
]