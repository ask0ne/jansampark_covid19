from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import RetailerForm

# Create your views here.

def index(request):
    return render(request, 'contributors/index.html')


def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RetailerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('contributors:index'))

    # if a GET (or any other method)
    else:
        form = RetailerForm()


    context = {'form': form}
    return render(request, 'contributors/entry_data.html', context)

