from django.contrib import admin

from online_store.products.models import Product, Order

admin.site.register(Product)
admin.site.register(Order)