# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-03 04:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='Indica el precio', max_length=100, verbose_name='Comentario')),
                ('costo', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='dise\xf1os', verbose_name='Im\xe1gen')),
            ],
        ),
        migrations.CreateModel(
            name='disenos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True, verbose_name='T\xedtulo')),
                ('descripcion', models.TextField()),
                ('presupuesto', models.IntegerField()),
                ('tiempo_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[(0, 'En proceso'), (1, 'Disponible')], max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disenos.disenos'),
        ),
    ]
