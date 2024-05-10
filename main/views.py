from django.shortcuts import render
from realtor.models import Properties
from django.views.generic import ListView, DetailView
from realtor.models import Properties

# Create your views here.
def base(request):
    props = Properties.objects.all()
    featured_props = Properties.objects.filter(featured=True)[0:3]

    context = {
        'props': props,
        'featured_props': featured_props
    }
    return render(request, 'base.html', context)


class PropertyListView(ListView):
    context_object_name = 'properties'
    model = Properties
    template_name = 'main/prop.html'
    paginate_by = 20


class PropertyDetailView(DetailView):
    context_object_name = 'property'
    model = Properties
    template_name = 'main/prop_details.html'