from django.contrib import admin
from.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=('title', 'price', 'description', 'image')
    search_fields = ['item_name',]

admin.site.register(Products, ProductsAdmin)

