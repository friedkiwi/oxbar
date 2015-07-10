# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('product_type', models.CharField(max_length=1, choices=[(b'S', b'Snack'), (b'D', b'Drink'), (b'A', b'Alcoholic Beverage')])),
                ('product_price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_sold', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('product_sold', models.ForeignKey(to='bar.Product')),
            ],
        ),
    ]
