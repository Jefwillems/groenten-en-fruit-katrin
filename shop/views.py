from django.http import HttpResponseForbidden
from django.views.generic import (TemplateView,
                                  FormView,
                                  ListView)
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from shop.forms import UpdatePricesForm, OrderForm
from shop.models import Item, ShoppingCartItem, ShoppingCart


class IndexView(TemplateView):
    template_name = 'shop/index.html'


class OrderView(FormMixin, ListView):
    template_name = 'shop/order.html'
    model = Item
    queryset = Item.objects.filter(published=True).order_by('name')
    context_object_name = 'items'
    form_class = OrderForm

    def get_success_url(self):
        return reverse(viewname='home')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        filtered = dict(
            (key.strip('amount-'), value) for (key, value) in form.cleaned_data.items() if value is not None)

        cart, created = ShoppingCart.objects.get_or_create(user=self.request.user, completed=False)
        cart.save()
        [ShoppingCartItem(product=Item.objects.get(plu_number=plu_number), amount=amount, cart=cart).save() for
         (plu_number, amount) in filtered.items()]

        return super(OrderView, self).form_valid(form)


class UploadPricesView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'shop/update_prices.html'
    form_class = UpdatePricesForm
    success_url = reverse_lazy('update-prices')

    def get_context_data(self, **kwargs):
        context = super(UploadPricesView, self).get_context_data(**kwargs)

        context['items'] = Item.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES.get('plu_file')
        if form.is_valid():
            for line in file:
                line_str = line.decode('utf-8')
                item = Item.from_plu_line(line_str)
                item.save()
            return self.form_valid(form)
        else:
            print(file)
            return self.form_invalid(form)
