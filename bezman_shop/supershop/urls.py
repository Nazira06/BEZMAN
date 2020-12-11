from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', orderList, name='orders'),
    path('order-create/<int:product_id>/', orderCreate, name='order-create'),
    path('order-update/<int:order_id>/', orderUpdate, name='order-update'),
    path('mf/', mf),
    path('vania/', vania),
    path('order-delete/<int:order_id>/', orderDelete, name='order-delete'),

]
