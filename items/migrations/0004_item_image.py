# Generated by Django 3.0.3 on 2020-02-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]