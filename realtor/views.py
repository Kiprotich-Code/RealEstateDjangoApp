from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import PropertiesForm

# Create your views here.
class realtor(TemplateView):
    template_name = "realtors/dashboard.html"

class CreatePropertyView(TemplateView):
    template_name = "realtors/create_property.html"
    form_class = PropertiesForm

