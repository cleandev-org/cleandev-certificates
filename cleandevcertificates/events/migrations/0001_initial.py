# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certified',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(null=True, verbose_name='classifica\xe7\xe3o', blank=True)),
                ('observation', models.TextField(verbose_name='observa\xe7\xe3o', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='alterado em')),
            ],
            options={
                'ordering': ['-event__date'],
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='nome')),
                ('workload', models.IntegerField(verbose_name='carga hor\xe1ria')),
                ('date', models.DateTimeField(verbose_name='data e hora')),
                ('complement', models.TextField(verbose_name='Complemento', blank=True)),
                ('post', models.URLField(verbose_name='Post', blank=True)),
                ('token', models.CharField(max_length=50, verbose_name='token', blank=True)),
                ('token_expirate', models.DateField(null=True, verbose_name='data de expira\xe7\xe3o', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='alterado em')),
                ('place', models.ForeignKey(related_name='place', verbose_name='Local', to='core.Person')),
                ('speaker', models.ForeignKey(related_name='speaker', verbose_name='Palestrante', to='core.Person')),
                ('support', models.ManyToManyField(to='core.Person', verbose_name='apoio')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='certified',
            name='event',
            field=models.ForeignKey(verbose_name='evento', to='events.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certified',
            name='person',
            field=models.ForeignKey(verbose_name='pessoa', to='core.Person'),
            preserve_default=True,
        ),
    ]
