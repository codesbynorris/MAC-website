from django.contrib import admin
from macapp.models import Inventory, Product, Shop

# Register your models here.
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Inventory)

