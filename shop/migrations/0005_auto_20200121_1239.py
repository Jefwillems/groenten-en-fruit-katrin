# Generated by Django 2.2.9 on 2020-01-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200121_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='plu_name',
            field=models.CharField(max_length=255),
        ),
    ]
