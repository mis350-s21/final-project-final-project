from django.urls import path
from .import views
urlpatterns = [
    path('', views.greeting, name='home'),
    path('product/<int:id>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]