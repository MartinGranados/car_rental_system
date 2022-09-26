# Generated by Django 2.2.1 on 2019-11-07 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_system', '0003_auto_20191107_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(500.0)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seats',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(12)]),
        ),
    ]