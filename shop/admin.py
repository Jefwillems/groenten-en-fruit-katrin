from django.contrib import admin
from shop.models import Item, PriceUnit

# Register your models here.
admin.site.register(Item)
admin.site.register(PriceUnit)
