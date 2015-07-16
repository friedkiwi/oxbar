# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_auto_20150710_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_tracker',
            field=models.IntegerField(default=0),
        ),
    ]
