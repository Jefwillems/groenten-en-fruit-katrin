from django.forms.widgets import NumberInput


class OrderItemWidget(NumberInput):
    template_name = 'shop/widgets/order_item_widget.html'

    def __init__(self, item, attrs=None):
        super(OrderItemWidget, self).__init__(attrs=attrs)
        self.item = item

    def get_context(self, name, value, attrs):
        context = super(OrderItemWidget, self).get_context(name, value, attrs)
        context['item'] = self.item
        return context
