# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('commodity_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('commodity_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'commodity_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyAlias',
            fields=[
                ('company_alias', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('company_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'company_alias_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConcessionAlias',
            fields=[
                ('concession_alias', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('concession_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'concession_alias_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
