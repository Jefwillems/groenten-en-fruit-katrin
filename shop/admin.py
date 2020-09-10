from django.contrib import admin
from django.db.models import QuerySet, Count
from django.shortcuts import render
import functools

from shop.models import Item, PriceUnit, ShoppingCart


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'plu_number', 'complete', 'published']

    class Meta:
        model = Item


class PriceUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'plu_shortcode']

    class Meta:
        model = PriceUnit


class ItemInline(admin.TabularInline):
    model = ShoppingCart.items.through
    extra = 0


class ShoppingCartAdmin(admin.ModelAdmin):
    fields = ('user', 'completed')
    list_display = ('user', 'completed')
    inlines = (ItemInline,)
    actions = ['mark_complete', 'mark_incomplete']

    def mark_incomplete(self, request, queryset: QuerySet):
        queryset.update(completed=False)
        return request

    mark_incomplete.short_description = 'Mark orders as incomplete.'

    def mark_complete(self, request, queryset: QuerySet):
        valid_orders = queryset.filter(completed=False)

        item_amounts = [x.get_items_counters() for x in valid_orders.all()]
        item_amounts = functools.reduce(lambda a, b: a.merge(b), item_amounts).item_amounts

        page = render(request, template_name='shop/export.html',
                      context={'carts': valid_orders, 'item_amounts': item_amounts})
        valid_orders.update(completed=True)

        return page

    mark_complete.short_description = 'Print and mark completed.'

    class Meta:
        model = ShoppingCart


admin.site.register(Item, ItemAdmin)
admin.site.register(PriceUnit, PriceUnitAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

admin.site.site_header = 'Groenten en fruit Katrin'
admin.site.site_title = 'Groenten en fruit Katrin'
admin.site.index_title = 'Groenten en fruit Katrin - admin'
