from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def puoductlist(reguest):
    products = Product.objects.all()
    context = {'products':products}
    return render(reguest,'supershop/products.html', context)

def orderList(reguest):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(reguest, 'supershop/order-List.html', context)

def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)

    form = OrderForm(initial={'product':product})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request,'supershop/order-created.html', context)