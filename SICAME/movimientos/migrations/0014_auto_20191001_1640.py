# Generated by Django 2.2.5 on 2019-10-01 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0013_auto_20191001_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='asig_id',
            field=models.ForeignKey(default=1, help_text='La devolucion debe conicidir con una Asignacion asicomo los elementos deben cuadrar', on_delete=django.db.models.deletion.CASCADE, to='movimientos.Asignacion', verbose_name='Ref. Asignacion'),
        ),
    ]
