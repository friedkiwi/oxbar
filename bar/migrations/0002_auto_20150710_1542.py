# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contains_milk',
            field=models.BooleanField(default=False, verbose_name=b'Milk ?'),
        ),
        migrations.AddField(
            model_name='product',
            name='contains_nuts',
            field=models.BooleanField(default=False, verbose_name=b'Nuts ?'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_vegan',
            field=models.BooleanField(default=False, verbose_name=b'Vegan ?'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_vegetarian',
            field=models.BooleanField(default=False, verbose_name=b'Vegetarian ?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
