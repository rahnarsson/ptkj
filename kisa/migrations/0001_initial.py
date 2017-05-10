# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kilpailu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=40)),
                ('vuosi', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kisaaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi_etu', models.CharField(max_length=30)),
                ('nimi_suku', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Laji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=50)),
                ('kilpailu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisa.Kilpailu')),
            ],
        ),
        migrations.CreateModel(
            name='LajiPisteet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pisteet', models.IntegerField(default=0)),
                ('kilpailu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisa.Kilpailu')),
                ('kisaaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisa.Kisaaja')),
                ('laji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kisa.Laji')),
            ],
        ),
    ]
