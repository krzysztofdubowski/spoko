# Generated by Django 3.1.7 on 2021-03-30 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RaportTransportowy', '0043_auto_20210325_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='PENDING',
            new_name='STATUS',
        ),
    ]
