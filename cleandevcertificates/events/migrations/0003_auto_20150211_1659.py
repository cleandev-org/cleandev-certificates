# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150211_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='token_expirate',
            field=models.DateField(null=True, verbose_name='data de expira\xe7\xe3o', blank=True),
        ),
    ]
