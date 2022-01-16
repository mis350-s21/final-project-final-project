from django.shortcuts import render , redirect
from .models import Products , Cart ,Comments
from .forms import  PaymentForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def greeting(request):
  product_objects = Products.objects.all()
  context ={
    'products': product_objects
  }

  return render(request, 'product.html', context)

def about(request):
  data={}
  return render(request, 'about.html', data)

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
@login_required(login_url='login')
def cart(request):
  userId = request.user.id
  if request.method == 'POST':
    itemId = int(request.POST.get('item_id'))
    quantity = int(request.POST.get('quantity'))
    addItem = Cart(customer_id = userId, product_id = itemId, quantity = quantity)
    addItem.save()
  cartItems = Cart.objects.filter(customer_id = userId)

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

def register(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  context = {
    'form': form
  }
  return render(request, 'register.html', context)

def login_request(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      print('not valid')
  return render(request, 'login.html')

def logout_request(request):
  logout(request)
  return redirect('home')