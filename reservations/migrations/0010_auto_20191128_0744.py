# Generated by Django 2.2.1 on 2019-11-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20191126_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_class',
            field=models.CharField(choices=[('Economy', 'Economy'), ('Standard', 'Standard'), ('Sport', 'Sport'), ('Luxury', 'Luxury')], default='Standard', max_length=9),
        ),
    ]
