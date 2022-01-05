from django.shortcuts import render
from .models import Order
# Create your views here.

def order_list(request):
    posts = Order.objects.all()
    c = {'order_list': Order,}
    return render(request, 'order_list.html', c)
