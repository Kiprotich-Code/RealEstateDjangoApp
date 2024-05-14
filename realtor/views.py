from django.shortcuts import render, redirect
from .forms import PropertiesForm
from django.views.generic import ListView, DetailView,  UpdateView
from .models import Properties
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def realtor(request):
    properties = Properties.objects.all()[0:9]
    context = {
        'properties': properties,
    }
    return render(request, 'realtors/dashboard.html', context)


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
    paginate_by = 5


class PropertyDetailView(DetailView):
    context_object_name = 'property'
    model = Properties
    template_name = 'realtors/property_details.html'


class PropertyUpdateView(UpdateView):
    template_name = 'realtors/update_property.html'
    model = Properties
    fields = ('title', 'description', 'images', 'address', 'price', 'size', 'status', 'location', 'featured', )
    success_url = '../property_list'