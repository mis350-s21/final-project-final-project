from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    # list_display = ('item_name','status','delivery_date')
    # list_filter =  ('item_name', )
    # search_fields = ['item_name',]
    pass
admin.site.register(Order, OrderAdmin)