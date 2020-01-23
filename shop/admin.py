from django.contrib import admin
from django.db.models import QuerySet, Count
from django.shortcuts import render

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

    mark_incomplete.short_description = 'Mark orders as incomplete'

    def mark_complete(self, request, queryset: QuerySet):
        valid_orders = queryset.filter(completed=False)

        shoppingcartitems_per_order = [x.shoppingcartitem_set.all() for x in valid_orders.all()]
        items_list = shoppingcartitems_per_order[0]
        for shoppingcartitems in shoppingcartitems_per_order[1:]:
            items_list = items_list | shoppingcartitems

        item_amounts = dict()
        for items in items_list:
            if items.product.name not in item_amounts:
                item_amounts[items.product.name] = 0
            item_amounts[items.product.name] += items.amount

        page = render(request, template_name='shop/export.html',
                      context={'carts': valid_orders, 'item_amounts': item_amounts})
        valid_orders.update(completed=True)

        return page

    mark_complete.short_description = 'Print and mark completed'

    class Meta:
        model = ShoppingCart


admin.site.register(Item, ItemAdmin)
admin.site.register(PriceUnit, PriceUnitAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

admin.site.site_header = 'Groenten en fruit Katrin'
admin.site.site_title = 'Groenten en fruit Katrin'
admin.site.index_title = 'Groenten en fruit Katrin - admin'
