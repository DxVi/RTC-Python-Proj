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







 