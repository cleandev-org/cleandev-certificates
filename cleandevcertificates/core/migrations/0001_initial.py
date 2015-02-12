# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default=b'S', max_length=1, verbose_name='tipo', choices=[(b'S', 'Aluno'), (b'U', 'Universidade'), (b'P', 'Patrocinador')])),
                ('course', models.CharField(max_length=100, verbose_name='curso', blank=True)),
                ('semester', models.IntegerField(null=True, verbose_name='semestre', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('display_name', models.CharField(max_length=100, verbose_name='apelido', blank=True)),
                ('cpf', models.CharField(max_length=20, null=True, verbose_name='CPF', blank=True)),
                ('email', models.EmailField(max_length=100, verbose_name='e-mail', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name='cidade', blank=True)),
                ('facebook', models.URLField(verbose_name='facebook', blank=True)),
                ('twitter', models.CharField(max_length=50, verbose_name='twitter', blank=True)),
                ('image', models.CharField(max_length=250, verbose_name='URL imagem', blank=True)),
                ('order', models.PositiveIntegerField(null=True, verbose_name='ordem de exibi\xe7\xe3o', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='alterador em')),
                ('university', models.ForeignKey(verbose_name='faculdade', blank=True, to='core.Person', null=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=(models.Model,),
        ),
    ]
