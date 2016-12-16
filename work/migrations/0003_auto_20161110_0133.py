# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20161110_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-added_date'], 'verbose_name_plural': 'Projects'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='in_development',
        ),
        migrations.RemoveField(
            model_name='project',
            name='media',
        ),
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AddField(
            model_name='project',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Gallery Image Title'),
        ),
        migrations.DeleteModel(
            name='Medium',
        ),
    ]
