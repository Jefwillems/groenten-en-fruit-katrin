# Generated by Django 2.2.9 on 2020-01-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200121_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
