# Generated by Django 2.2.9 on 2020-01-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priceunit',
            old_name='shortcode',
            new_name='plu_shortcode',
        ),
        migrations.AddField(
            model_name='priceunit',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
