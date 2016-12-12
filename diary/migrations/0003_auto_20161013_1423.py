# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20161012_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='types',
            name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='some_event',
            new_name='describe_event',
        ),
        migrations.AlterField(
            model_name='event',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Stripe'),
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
