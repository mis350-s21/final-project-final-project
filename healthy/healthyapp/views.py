from django.shortcuts import render
from .models import Products

# Create your views here.
def greeting(request):
  product_objects = Products.objects.all()
  context ={
    'products': product_objects
  }

  return render(request, 'product.html', context)

def search(request):
  products = Products.objects.all()
  if 'item_name' in request.POST:
    item_name = request.POST.get('item_name')
    if item_name: 
      context = {
        "products": products.filter(title__contains = item_name)
      }
    else: 
      context = {
        "products": products
      }

    return render(request, ' search_product.html', context)
