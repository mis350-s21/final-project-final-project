from django.shortcuts import render , redirect
from .models import Products , Cart ,Comments
from .forms import  PaymentForm, ContactForm

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

    return render(request, 'search_product.html', context)

def cart(request):
  if request.method == 'POST':
    itemId = int(request.POST.get('item_id'))
    addItem = Cart(product_id = itemId)
    addItem.save()
  cartItems = Cart.objects.all()
  context = {
    'items': cartItems
  }
  

  return render(request, 'cart.html', context)

def checkout(request):

  pay = PaymentForm(request.POST or None)
  if pay.is_valid():
    pay.save()
    return redirect('home')

  cartItems = Cart.objects.all()
  itemsCount = cartItems.count()
  
  total = 0
  for item in cartItems:
    total += float(item.product.price)

  print(total)
  context = {
    'total': itemsCount,
    'totalprice': total,
    'form': PaymentForm
  }
  return render(request,'checkout.html', context)


def contact(request):
  leaveComment = ContactForm(request.POST)
  if leaveComment.is_valid():
    leaveComment.save()

  contactForm = {
    'form': ContactForm
  }


  return render(request, 'contact.html', contactForm)