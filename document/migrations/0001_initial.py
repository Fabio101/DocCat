# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20151104_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120)),
                ('description', models.TextField(max_length=2000)),
                ('document', models.FileField(upload_to=b'document/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('catalogue', models.ForeignKey(to='catalogue.Catalogue')),
            ],
        ),
    ]
