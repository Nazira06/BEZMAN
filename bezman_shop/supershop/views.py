from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def puoductlist(reguest):
    products = Product.objects.all()
    context = {'products': products}
    return render(reguest, 'supershop/products.html', context)

def orderList(reguest):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    #orders_in_process =

    context = {'orders': orders, 'orders_count': orders.count, 'orders_delivered': orders_delivered}
    return render(reguest, 'supershop/order-List.html', context)

def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)

    form = OrderForm(initial={'product': product})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request,'supershop/order-created.html', context)

def orderUpdate(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'supershop/order-created.html', context)
