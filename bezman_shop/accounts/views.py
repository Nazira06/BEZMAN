from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .decorators import admin_only
from .models import *


# Create your views here.
@admin_only
def customerList(reguest):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(reguest, 'accounts/customer.html', context)

def getCustomer(reguest,customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExsist:
        return HttpResponse('page status 404')
    orders = customer.order_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(reguest, 'accounts/getcustomer.html', context)


def userCreated(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='bezgirl')
            user.groups.add(group)
            Customer.objects.create(user=user, phone=1, full_name=user.username)
            user.save
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/user-created.html', context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
    context = {}
    return render(request, 'accounts/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
