from django.shortcuts import render
# from django.http import HttpResponse
from .weather import weather_scrape


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def officers(request):
    return render(request, 'officers.html')

def services(request):
    return render(request, 'services.html')    

def newsevents(request):
    return render(request, 'newsevents.html')

def weather(request):
    testvar = weather_scrape() + " | hello from view.py.."
    return render(request, 'weather.html', {'varx': testvar})  