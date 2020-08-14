from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


def category(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'category.html', {'categories': categories})


def product(request):
    category_id = request.GET.get('id')
    categories = Category.objects.filter(id=category_id)
    products = Product.objects.filter(category=category_id)
    return render(request, 'product.html', {'products': products, 'categories':categories})


def newsevents(request):
    return render(request, 'newsevents.html')


def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')


def officers(request):
    return render(request, 'officers.html')

def services(request):
    return render(request, 'services.html')    

def contact(request):
    return render(request, 'contact.html')

 