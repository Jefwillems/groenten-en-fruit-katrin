from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import ShopUserCreationForm, ShopUserChangeForm
from users.models import ShopUser


class ShopUserAdmin(UserAdmin):
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm
    model = ShopUser
    list_display = ['email', 'username']


admin.site.register(ShopUser, ShopUserAdmin)
