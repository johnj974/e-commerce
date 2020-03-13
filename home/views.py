from django.shortcuts import render

# Create your views here.


# a view to render a home page
def index(request):
    return render(request, 'index.html')
