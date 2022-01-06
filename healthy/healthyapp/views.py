from django.shortcuts import render
from .models import Products
# Create your views here.
def greeting(request):
    data={}
    p = Products.objects.all()
    data['pro'] = p
    data['m'] = 'Hello'
    return render(request, 'product.html', context=data)