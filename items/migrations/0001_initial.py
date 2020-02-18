# Generated by Django 3.0.3 on 2020-02-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, editable=False, max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('S', 'shirts'), ('OW', 'Outwear'), ('SW', 'Sports')], max_length=2)),
            ],
        ),
    ]