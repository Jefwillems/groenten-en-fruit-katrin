# Generated by Django 2.2.9 on 2020-01-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200114_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='produce'),
        ),
    ]