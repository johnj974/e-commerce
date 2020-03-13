from django.contrib import admin
from .models import Product             # product class/object imported from models.py

# Register your models here so that we can access it from the admin panel
admin.site.register(Product)
