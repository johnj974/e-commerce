from django.shortcuts import render
from products.models import Product     # product class from the product app

# Create your views here.


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])     # filter is a built in function
    return render(request, "products.html", {"products": products})
