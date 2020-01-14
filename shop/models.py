from django.db import models


class PriceUnit(models.Model):
    shortcode = models.CharField(max_length=30)


class Item(models.Model):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(PriceUnit, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    plu_number = models.IntegerField()
    image = models.ImageField(null=True, default=None, upload_to='produce')
