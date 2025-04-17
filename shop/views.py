from django.shortcuts import render
from .models import Products
# Create your views here.
def index(request):
    Product_objects = Products.objects.all()
    return render(request, 'shop/index.html', {'Product_objects': Product_objects})