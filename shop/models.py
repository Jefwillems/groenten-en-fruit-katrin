from django.db import models
from decimal import Decimal

from users.models import ShopUser


class PriceUnit(models.Model):
    plu_shortcode = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(PriceUnit, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    plu_number = models.IntegerField(unique=True)
    plu_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, default=None, upload_to='produce')
    description = models.TextField(blank=True, default='')
    complete = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    @staticmethod
    def from_plu_line(line):
        a = line.split(';')
        line_values = [x.rstrip(' ') for x in a]

        plu_name = line_values[4]
        unit, created_unit = PriceUnit.objects.get_or_create(plu_shortcode=line_values[9])
        price = line_values[6]
        price = price.replace(',', '.')
        price = Decimal(price)
        plu_number = int(line_values[3])

        item = Item.objects.filter(plu_name=plu_name, plu_number=plu_number).first()
        if item:
            # Item exists already, updating item
            item.plu_name = plu_name
            item.plu_number = plu_number
            if created_unit:
                item.complete = False
                item.published = False
            item.unit = unit
            item.price = price
        else:
            # Item does not exist, creating a new one.
            item = Item.objects.create(name=plu_name,
                                       unit=unit,
                                       price=price,
                                       plu_number=plu_number,
                                       plu_name=plu_name)
        return item

    def __str__(self):
        return f'Item: {self.plu_number}/{self.name}'


class ShoppingCart(models.Model):
    user = models.OneToOneField(to=ShopUser, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(to=Item, through='ShoppingCartItem')
    completed = models.BooleanField(default=False)


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(to=ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Item, on_delete=models.CASCADE, related_name='+')
    amount = models.IntegerField(default=0)
