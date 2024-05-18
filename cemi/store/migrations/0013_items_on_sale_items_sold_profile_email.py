# Generated by Django 4.2.11 on 2024-05-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='on_sale',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='sold',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
