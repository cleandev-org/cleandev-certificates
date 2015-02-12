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
            name='display_name',
            field=models.CharField(max_length=100, verbose_name='apelido', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='kind',
            field=models.CharField(default=b'S', max_length=1, verbose_name='tipo', choices=[(b'S', 'Aluno'), (b'U', 'Universidade'), (b'P', 'Patrocinadores')]),
        ),
    ]
