from django.shortcuts import render
from .models import Country

# Create your views here.
def home(request):
    countries = Country.objects.all()
    rest_countries_api = "https://restcountries.com/v3.1/all"
    return render(request, 'index.html', {"countries": countries})
