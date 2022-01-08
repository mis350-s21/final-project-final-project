from django import forms
from django.db.models.fields import files
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
       