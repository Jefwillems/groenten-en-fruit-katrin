from django.contrib import admin
from shop.models import Item, PriceUnit

# Register your models here.
admin.site.register(Item)
admin.site.register(PriceUnit)

admin.site.site_header = 'Groenten en fruit Katrin'
admin.site.site_title = 'Groenten en fruit Katrin'
admin.site.index_title = 'Groenten en fruit Katrin - admin'
