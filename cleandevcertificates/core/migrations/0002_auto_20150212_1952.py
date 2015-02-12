# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(default=2, max_length=20, verbose_name='CPF', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(default=3, verbose_name='ordem de exibi\xe7\xe3o'),
            preserve_default=False,
        ),
    ]
