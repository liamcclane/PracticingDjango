# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-07 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255)),
                ('age', models.SmallIntegerField(verbose_name=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=45)),
                ('pet', models.CharField(blank=True, default=None, max_length=45, null=True)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
