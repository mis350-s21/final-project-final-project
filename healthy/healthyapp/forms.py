from django import forms
from .models import Products , Comments,Payment



class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'email', 'mobile', 'method']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'


