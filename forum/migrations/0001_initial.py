# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=9999)),
            ],
        ),
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('nick', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(verbose_name='Registration date')),
            ],
        ),
        migrations.AddField(
            model_name='forumpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.ForumUser'),
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.ForumPost'),
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.ForumUser'),
        ),
    ]
