# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pg.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0002_commodity_companyalias_concessionalias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('label', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('metadata', django_pg.models.fields.json.JSONField(blank=True, default='{}', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sequencenum', models.IntegerField()),
                ('metadata', django_pg.models.fields.json.JSONField(blank=True, default='{}', null=True)),
                ('search', models.ForeignKey(to='hulk.Search')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
