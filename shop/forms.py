from django import forms
from shop.models import Item
from shop.widgets import OrderItemWidget


class UpdatePricesForm(forms.Form):
    plu_file = forms.FileField(required=True,
                               allow_empty_file=False,
                               widget=forms.ClearableFileInput(attrs={'accept': '.TXT,.txt,text/plain'}))


class OrderForm(forms.Form):
    remarks = forms.CharField(required=False, label='Opmerkingen', widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        items = Item.objects.filter(published=True, complete=True)
        self.field_order = []
        for item in items:
            item_html_id = f'amount-{item.plu_number}'
            self.fields[item_html_id] = forms.IntegerField(required=False, min_value=0, label=False,
                                                           widget=OrderItemWidget(item, attrs={'value': 0}))
            self.field_order.append(item_html_id)
        self.field_order.append('remarks')
        self.order_fields(self.field_order)
