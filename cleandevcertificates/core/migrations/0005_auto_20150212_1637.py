# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150211_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['order', 'name'], 'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(null=True, verbose_name='ordem de exibi\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='kind',
            field=models.CharField(default=b'S', max_length=1, verbose_name='tipo', choices=[(b'S', 'Aluno'), (b'U', 'Universidade'), (b'P', 'Patrocinador')]),
            preserve_default=True,
        ),
    ]
