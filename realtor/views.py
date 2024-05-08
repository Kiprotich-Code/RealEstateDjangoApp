from django.shortcuts import render, redirect
from .forms import PropertiesForm
from django.views.generic import ListView, DetailView,  UpdateView
from .models import Properties

# Create your views here.
def realtor(request):
    return render(request, 'realtors/dashboard.html')


def create_property(request):
    if request.method == 'POST':
        form = PropertiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')

    else:
        form = PropertiesForm()

    context = {
        'form': form,
    }

    return render(request, 'realtors/create_property.html', context)

class PropertyListView(ListView):
    context_object_name = 'properties'
    model = Properties
    template_name = 'realtors/property_list.html'


class PropertyDetailView(DetailView):
    context_object_name = 'property'
    model = Properties
    template_name = 'realtors/property_details.html'


class PropertyUpdateView(UpdateView):
    template_name = 'realtors/update_property.html'
    model = Properties
    fields = ('title', 'description', 'images', 'features')
    success_url = '../property_list'