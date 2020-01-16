from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email')


class ShopUserChangeForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email')
