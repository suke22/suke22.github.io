# Generated by Django 4.2 on 2023-04-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subir_datos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato',
            name='agenda',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='AGENDA'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='cp',
            field=models.PositiveBigIntegerField(verbose_name='CÓDIGO POSTAL'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='dia_cita',
            field=models.DateTimeField(verbose_name='CITA'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='direccion',
            field=models.CharField(max_length=200, verbose_name='DIRECCIÓN'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='estado',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ESTADO'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='movil',
            field=models.PositiveBigIntegerField(verbose_name='MÓVIL'),
        ),
        migrations.AlterField(
            model_name='dato',
            name='nhc',
            field=models.CharField(max_length=10, verbose_name='NHC'),
        ),
    ]
