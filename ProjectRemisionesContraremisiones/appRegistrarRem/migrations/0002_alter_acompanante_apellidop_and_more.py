# Generated by Django 4.0.4 on 2022-06-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appRegistrarRem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompanante',
            name='apellidoP',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='apellidoS',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Apellido'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='direccionHabitual',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección de residencia'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='municipioHabitual',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Municipio de residencia'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='nombreP',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='nombreS',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='parentesco_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.parentesco'),
        ),
        migrations.AlterField(
            model_name='acompanante',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='telefono'),
        ),
    ]