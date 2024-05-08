from django.shortcuts import render
from realtor.models import Properties
from django.views.generic import ListView, DetailView

# Create your views here.
def base(request):
    return render(request, 'base.html')


class PropertyListView(ListView):
    context_object_name = 'properties'
    model = Properties
    template_name = 'main/prop.html'


class PropertyDetailView(DetailView):
    context_object_name = 'property'
    model = Properties
    template_name = 'main/prop_details.html'