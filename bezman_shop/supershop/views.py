from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter

# Create your views here.
def puoductlist(reguest):
    products = Product.objects.all()
    filter = ProductFilter(reguest.GET, queryset=products)
    products = filter.qs
    context = {'products': products, 'filter': filter}
    return render(reguest, 'supershop/products.html', context)

def orderList(reguest):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_in_process = Order.objects.filter(status='In Process').count()
    orders_not_delivered = Order.objects.filter(status='Not Delivered').count()

    context = {'orders': orders, 'orders_count': orders.count, 'orders_delivered': orders_delivered,
               'orders_in_process':  orders_in_process,  'orders_not_delivered':  orders_not_delivered,
               }
    return render(reguest, 'supershop/order-List.html', context)

def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user
    form = OrderForm(initial={'product': product, 'customer': customer})

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
