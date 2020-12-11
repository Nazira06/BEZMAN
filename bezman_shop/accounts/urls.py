from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('customers/', customerList, name='customer'),
    path('customers/<int:customer_id>/', getCustomer, name='getcustomer'),
    path('user-created/', userCreated, name='user-created'),
    path('login/', auth, name='login'),
    path('logout/', logout_page, name='logout'),



]
