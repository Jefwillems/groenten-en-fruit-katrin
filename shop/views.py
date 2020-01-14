from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'shop/index.html'


class OrderView(TemplateView):
    template_name = 'shop/order.html'
