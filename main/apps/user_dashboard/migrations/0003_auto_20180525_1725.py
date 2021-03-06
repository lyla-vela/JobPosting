# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0002_auto_20180524_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uploaded_by_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_jobs', to='user_dashboard.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='liked_by_id',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='uploaded_by_id',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
