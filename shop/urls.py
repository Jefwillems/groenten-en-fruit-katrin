from django.urls import path
from shop.views import IndexView, OrderView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('order', OrderView.as_view(), name='order')
]
