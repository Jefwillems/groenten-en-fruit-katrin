from django.urls import path
from shop.views import IndexView, OrderView, UploadPricesView, ShoppingCartView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('order', OrderView.as_view(), name='order'),
    path('update/', UploadPricesView.as_view(), name='update-prices'),
    path('shoppingcart/', ShoppingCartView.as_view(), name='cart')
]
