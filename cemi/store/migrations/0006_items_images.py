# Generated by Django 4.2.13 on 2024-05-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_items_discount_items_percentage_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='images',
            field=models.ImageField(default='fridge.jpg', null=True, upload_to='static/'),
        ),
    ]