from django.conf.urls import url        # importing the main urls
from .views import do_search            # importing the search view from the search views.py file


# url pattern for search view
urlpatterns = [
    url(r'^$', do_search, name='search')
]