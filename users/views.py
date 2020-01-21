from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from users.forms import ShopUserChangeForm, ShopUserCreationForm


class RegisterView(FormView):
    form_class = ShopUserCreationForm


class ShopLoginView(LoginView):
    template_name = 'users/login.html'


class ShopLogoutView(LogoutView):
    pass


class ShopPasswordChangeView(PasswordChangeView):
    pass


class ProfileView(FormView):
    form_class = ShopUserChangeForm
