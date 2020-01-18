from django.db import models
from decimal import Decimal

from users.models import ShopUser


class PriceUnit(models.Model):
    shortcode = models.CharField(max_length=30)


class Item(models.Model):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(PriceUnit, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    plu_number = models.IntegerField(unique=True)
    plu_name = models.CharField(unique=True, max_length=255)
    image = models.ImageField(blank=True, default=None, upload_to='produce')

    @staticmethod
    def from_plu_line(line):
        a = line.split(';')
        line_values = [x.rstrip(' ') for x in a]
        plu_name = line_values[4]
        unit = line_values[9]
        price = line_values[6]
        price = price.replace(',', '.')
        price = Decimal(price)
        plu_number = int(line_values[3])
        item = Item.objects.filter(plu_name=plu_name, plu_number=plu_number).first()
        if item:
            print(plu_name, unit, price, plu_number)
        return ''


class ShoppingCart(models.Model):
    user = models.OneToOneField(to=ShopUser, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(to=Item, through='ShoppingCartItem')


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(to=ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Item, on_delete=models.CASCADE, related_name='+')
    amount = models.IntegerField(default=0)
