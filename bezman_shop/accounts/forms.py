from django.forms import ModelForm
from .models import Customer


class UserProfile(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user',]