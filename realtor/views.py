from django.shortcuts import render, redirect
from .forms import PropertiesForm

# Create your views here.
def realtor(request):
    return render(request, 'realtors/dashboard.html')


def create_property(request):
    if request.method == 'POST':
        form = PropertiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('realtor')
        
    else:
        form = PropertiesForm()

    context = {
        'form': form,
    }

    return render(request, 'realtors/create_property.html', context)