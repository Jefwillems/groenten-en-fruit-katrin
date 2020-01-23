from django import forms
from shop.models import Item


class UpdatePricesForm(forms.Form):
    plu_file = forms.FileField(required=True,
                               allow_empty_file=False,
                               widget=forms.ClearableFileInput(attrs={'accept': '.TXT,.txt,text/plain'}))


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        items = Item.objects.only('plu_number')
        for item in items:
            self.fields[f'amount-{item.plu_number}'] = forms.IntegerField(required=False, min_value=0)
