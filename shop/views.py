from django.views.generic import (TemplateView,
                                  FormView,
                                  ListView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from shop.forms import UpdatePricesForm
from shop.models import Item
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'shop/index.html'


class OrderView(ListView):
    template_name = 'shop/order.html'
    model = Item
    queryset = Item.objects.all().order_by('name')
    context_object_name = 'items'


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
                Item.from_plu_line(line_str)
            return self.form_valid(form)
        else:
            print(file)
            return self.form_invalid(form)
