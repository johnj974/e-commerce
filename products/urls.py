from django.conf.urls import url, include
from .views import all_products


# this will show the all products view
urlpatterns = [
    url(r'^$', all_products, name='products'),
]