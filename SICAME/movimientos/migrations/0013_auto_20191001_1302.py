# Generated by Django 2.2.5 on 2019-10-01 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0012_auto_20191001_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material_devuelto',
            old_name='totalXD',
            new_name='total',
        ),
    ]
