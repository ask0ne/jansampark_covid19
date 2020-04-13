from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import RetailerForm
from django.contrib.auth.models import User
from retailers.models import Retailer 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

@login_required
def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if User.objects.filter(username=request.POST["company_name"]).exists():
            company_name = request.POST["company_name"]
            product = request.POST["product"]
            quantity = request.POST["quantity"]
            lat = request.POST["lat"]
            long= request.POST["long"]

            record = Retailer(company_name=company_name, product=product, quantity=quantity, lat=lat, long=long)
            record.save()
            # form = RetailerForm(request.POST)
        # check whether it's valid:
            # if form.is_valid():
                # process the data in form.cleaned_data as required
                # redirect to a new URL:
                # form.save()
            return HttpResponseRedirect(reverse('frontend:index'))

    # if a GET (or any other method)
    form = RetailerForm()


    context = {'form': form}
    return render(request, 'frontend/entry_data.html', context)
