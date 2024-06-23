# Generated by Django 2.2.14 on 2024-06-23 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dirrecion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direcion_estado', models.CharField(max_length=150)),
                ('direcion_municipio', models.CharField(max_length=150)),
                ('direcion_sector', models.CharField(max_length=150)),
                ('direcion_casa', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Mercancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wehrehouse_creado', models.BooleanField(default=False, verbose_name='Creacion')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('trakin', models.IntegerField(verbose_name='codigo de paquete')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre del cliente')),
                ('Apellido', models.CharField(max_length=150, verbose_name='Apellido del cliente')),
                ('cedula', models.CharField(max_length=150, verbose_name='cedulo o del cliente')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('correo_aux', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=150)),
                ('telefono_aux', models.CharField(max_length=150)),
                ('tipo_cliente', models.CharField(choices=[('cliente1', 'Cliente Normal'), ('Cliente2', 'Ejecutivo')], max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wehrehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(choices=[('Persona', 'Persona Natural'), ('Empresa', 'Persona Juridica')], max_length=60)),
                ('shipper', models.CharField(blank=True, max_length=150)),
                ('recibido_de', models.CharField(max_length=150)),
                ('persona_recibe', models.CharField(max_length=150)),
                ('peso_caja', models.FloatField()),
                ('ancho_caja', models.FloatField()),
                ('profundida_caja', models.FloatField()),
                ('pago', models.FloatField()),
                ('Tracking_num', models.IntegerField(verbose_name='')),
                ('contenido', models.CharField(max_length=150)),
                ('valor', models.FloatField()),
                ('comentarios', models.TextField()),
                ('onservaciones', models.TextField()),
                ('regisro_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.RegistroCliente', verbose_name='registro cliente')),
            ],
        ),
    ]
