from django.urls import path
from . import views

urlpatterns = [
    path('', views.category),             #base.html     /products
    path('category/', views.product),     #category.html /category/?name=categoryname
    
]