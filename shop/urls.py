from django.urls import path
from shop.views import IndexView, OrderView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', IndexView.as_view(), name='home'),
                  path('order', OrderView.as_view(), name='order')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
