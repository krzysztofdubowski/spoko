# Generated by Django 3.1.7 on 2021-03-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaportTransportowy', '0026_auto_20210318_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='ILOSC_PALET',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
