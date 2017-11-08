# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Encabezado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('encargado', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='encabezado',
            name='materiales',
            field=models.ManyToManyField(through='PROYECTO_APP.Descripcion', to='PROYECTO_APP.Material'),
        ),
        migrations.AddField(
            model_name='descripcion',
            name='encabezado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROYECTO_APP.Encabezado'),
        ),
        migrations.AddField(
            model_name='descripcion',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PROYECTO_APP.Material'),
        ),
    ]