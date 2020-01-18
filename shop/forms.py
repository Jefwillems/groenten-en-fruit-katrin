from django import forms


class UpdatePricesForm(forms.Form):
    plu_file = forms.FileField(required=True,
                               allow_empty_file=False,
                               widget=forms.ClearableFileInput(attrs={'accept': '.TXT,.txt,text/plain'}))
