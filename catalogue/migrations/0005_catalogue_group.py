# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('catalogue', '0004_auto_20151110_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='group',
            field=models.ForeignKey(default=1, to='auth.Group', null=True),
        ),
    ]
