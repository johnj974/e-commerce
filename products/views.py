from django.shortcuts import render
from .models import Product                         #import our product object from models

# Create your views here.


# this view will return all the products in the database
def all_products(request):
    products = Product.objects.all()                # access to all products here
    return render(request, "products.html", {"products": products})         # generates html and all products