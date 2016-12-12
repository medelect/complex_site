# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=50)),
                ('mail', models.IntegerField(verbose_name='Email')),
                ('phone_number', models.IntegerField()),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(max_length=50)),
                ('some_event', models.CharField(max_length=500)),
                ('start_time', models.DateTimeField(verbose_name='date published')),
                ('limit', models.DateTimeField(verbose_name='date published')),
                ('importance', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Event')),
            ],
        ),
    ]
