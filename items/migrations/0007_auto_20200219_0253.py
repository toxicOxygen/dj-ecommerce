# Generated by Django 3.0.3 on 2020-02-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200219_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=200, unique=True),
        ),
    ]