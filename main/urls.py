from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),

    # Cbvs 
    path('props/', views.PropertyListView.as_view(), name='props'),
    path('prop_details/<pk>', views.PropertyDetailView.as_view(), name='prop_details'),
]