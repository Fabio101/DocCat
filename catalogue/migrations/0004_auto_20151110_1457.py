# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20151109_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
