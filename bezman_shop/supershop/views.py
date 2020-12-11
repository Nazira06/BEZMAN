from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter
from .decorators import allowed_roles

# Create your views here.
def puoductlist(reguest):
    products = Product.objects.all()
    filter = ProductFilter(reguest.GET, queryset=products)
    products = filter.qs
    context = {'products': products, 'filter': filter}
    return render(reguest, 'supershop/products.html', context)

@allowed_roles(allowed=['bezman'])
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
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExsist:
        return HttpResponse('page status 404')
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
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExsist:
        return HttpResponse('page status 404')
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'supershop/order-created.html', context)

def mf(request):
    string = "wjmzbmr"
    a = set(string)
    if len(a)%2==0:
        return HttpResponse('CHAT WITH HER')
    else:

        return HttpResponse('CHAT WITH HIM')


def vania(request):
    import random
    n,h = 3,7
    list1 = []
    list2 = [4, 5, 14]
    # for i in range(n):
    #     list1.append(random.randint(1, 20))
    for hei in list2:
        if hei > h:
            list1.append(2)
        elif hei <= h:
            list1.append(1)
    return HttpResponse(sum(list1))

def orderDelete(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('page status 404')

    form = OrderForm(instance=order)
    if request.method == 'POST':
        if order.status == 'Not Delivered':
            order.delete()

            return HttpResponse('Order Deleted!')

        else:
            return HttpResponse('Order Deleted!')

    context = {'order':order}
    return render(request,'supershop/order-delete.html', context)






