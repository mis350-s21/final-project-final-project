from django import forms
from django.db.models.fields import files
from .models import Products , Payment



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'email', 'mobile', 'method']