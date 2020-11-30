from django.shortcuts import render
from .models import *

# Create your views here.
def puoductlist(reguest):
    puoducts = Product.objects.all()
    return render(reguest,'supershop/products.html')