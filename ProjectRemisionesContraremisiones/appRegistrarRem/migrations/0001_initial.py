# Generated by Django 4.0.4 on 2022-05-26 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numIdentificacion', models.CharField(max_length=50, verbose_name='Número identificación')),
                ('nombreP', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('nombreS', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('apellidoP', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('apellidoS', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('municipioHabitual', models.CharField(max_length=50, verbose_name='Municipio de residencia')),
                ('direccionHabitual', models.CharField(max_length=50, verbose_name='Dirección de residencia')),
                ('telefono', models.CharField(max_length=50, verbose_name='telefono')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Acompañante',
                'verbose_name_plural': 'Acompañantes',
            },
        ),
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numCarnet', models.CharField(max_length=50, verbose_name='Número de carné')),
                ('numIdentificacion', models.CharField(max_length=50, verbose_name='Número identificación')),
                ('nombreP', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('nombreS', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('apellidoP', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('apellidoS', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('genero', models.CharField(max_length=50, verbose_name='genero')),
                ('fechaNacimiento', models.DateField(max_length=50, verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=50, verbose_name='telefono')),
                ('regimen', models.CharField(max_length=50, verbose_name='Régimen')),
                ('municipioHabitual', models.CharField(max_length=50, verbose_name='Municipio de residencia')),
                ('direccionHabitual', models.CharField(max_length=50, verbose_name='Dirección de residencia')),
                ('ipsPrimaria', models.CharField(max_length=50, verbose_name='IPS primaria')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado afiliación')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Afiliado',
                'verbose_name_plural': 'Afiliados',
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Parentesco')),
            ],
            options={
                'verbose_name': 'Parentesco',
                'verbose_name_plural': 'Parentescos',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numIdentificacion', models.CharField(max_length=50, verbose_name='Número identificación')),
                ('nombreP', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('nombreS', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('apellidoP', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('apellidoS', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('telefono', models.CharField(max_length=50, verbose_name='telefono')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Tipo identificación')),
            ],
            options={
                'verbose_name': 'TipoIdentificacion',
                'verbose_name_plural': '-TipoIdentificaciones',
            },
        ),
        migrations.CreateModel(
            name='Remision_Contraremision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RemiContId', models.CharField(max_length=50, verbose_name='Id remision')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('Acom_numIdentificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.acompanante')),
                ('Afil_numIdentificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.afiliado')),
                ('Prof_numIdentificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.profesional')),
            ],
            options={
                'verbose_name': 'remision',
                'verbose_name_plural': 'remisiones',
            },
        ),
        migrations.AddField(
            model_name='afiliado',
            name='tipoIdentificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.tipoidentificacion'),
        ),
        migrations.AddField(
            model_name='acompanante',
            name='parentesco_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.parentesco'),
        ),
        migrations.AddField(
            model_name='acompanante',
            name='tipoIdentificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRegistrarRem.tipoidentificacion'),
        ),
    ]
