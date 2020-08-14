from django.urls import path
from . import views

urlpatterns = [
    path('', views.category),             #base.html     /products
    path('category/', views.product),     #category.html /category/?name=categoryname
    path('newsevents/', views.newsevents),
    path('about/', views.about),
    path('faq/', views.faq),
    path('officers/', views.officers),
    path('services/', views.services),
    path('contact/', views.contact),
]