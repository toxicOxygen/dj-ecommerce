# Generated by Django 3.0.3 on 2020-02-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20200219_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirts'), ('OW', 'Outwear'), ('SW', 'Sports'), ('MJ', "Men's Jewelry"), ('F', 'Fashion'), ('W', 'Watches')], max_length=2),
        ),
    ]
