# Generated by Django 3.0 on 2020-04-18 04:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200416_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzas',
            name='photo',
            field=models.ImageField(default='main/img/pizza.jpg', upload_to='main/img'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 4, 44, 6, 186719, tzinfo=utc), verbose_name='Date Ordered'),
        ),
    ]