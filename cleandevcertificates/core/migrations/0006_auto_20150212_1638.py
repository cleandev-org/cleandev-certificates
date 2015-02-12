# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150212_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.CharField(max_length=250, verbose_name='URL imagem', blank=True),
            preserve_default=True,
        ),
    ]
