# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20151104_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
