# Generated by Django 3.0.3 on 2020-02-19 03:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20200219_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
