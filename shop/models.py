from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=30)  # TODO: choice
    price = models.DecimalField(decimal_places=2, max_digits=6)
    plu_number = models.IntegerField()
