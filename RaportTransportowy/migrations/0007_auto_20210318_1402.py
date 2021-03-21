# Generated by Django 3.1.7 on 2021-03-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaportTransportowy', '0006_auto_20210318_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='CAŁOPOJAZDOWE',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transport',
            name='PENDING',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('ZREA:LIZOWANE', 'ZREALIZOWANE'), ('FAKTURA', 'FAKTURA')], max_length=100),
        ),
    ]
