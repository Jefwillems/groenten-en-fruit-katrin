from django.views.generic import TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.forms import UpdatePricesForm
from shop.models import Item
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'shop/index.html'


class OrderView(TemplateView):
    template_name = 'shop/order.html'


class UploadPricesView(LoginRequiredMixin, FormView):
    template_name = 'shop/update_prices.html'
    form_class = UpdatePricesForm
    success_url = reverse_lazy('update-prices')

    def get_context_data(self, **kwargs):
        context = super(UploadPricesView, self).get_context_data(**kwargs)

        context['items'] = Item.objects.all()

        return context

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
