# Generated by Django 3.1.7 on 2021-03-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaportTransportowy', '0007_auto_20210318_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='CAŁOPOJAZDOWE',
            field=models.BooleanField(default=False),
        ),
    ]
