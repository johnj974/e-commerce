

from django.db import models


# This is the model created for our product display, it has a name field, description area,price and image
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    # a function to return a string with the name
    
    def __str__(self):
        return self.name