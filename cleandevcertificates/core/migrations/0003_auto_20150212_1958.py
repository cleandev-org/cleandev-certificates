# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150212_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='ordem de exibi\xe7\xe3o'),
            preserve_default=True,
        ),
    ]
