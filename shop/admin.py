from django.contrib import admin
from shop.models import Item, PriceUnit


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'plu_number', 'complete', 'published']

    class Meta:
        model = Item


class PriceUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'plu_shortcode']

    class Meta:
        model = PriceUnit


admin.site.register(Item, ItemAdmin)
admin.site.register(PriceUnit, PriceUnitAdmin)

admin.site.site_header = 'Groenten en fruit Katrin'
admin.site.site_title = 'Groenten en fruit Katrin'
admin.site.index_title = 'Groenten en fruit Katrin - admin'
