from django.contrib import admin
from shop.models import Item, PriceUnit


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'plu_number']

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)
admin.site.register(PriceUnit)

admin.site.site_header = 'Groenten en fruit Katrin'
admin.site.site_title = 'Groenten en fruit Katrin'
admin.site.index_title = 'Groenten en fruit Katrin - admin'
