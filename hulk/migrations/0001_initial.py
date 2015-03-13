# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('open_lei_id', models.CharField(max_length=200, blank=True)),
                ('duns_number', models.CharField(max_length=200, blank=True)),
                ('company_name', models.CharField(max_length=200)),
                ('ticker_symbol', models.CharField(max_length=200, blank=True)),
                ('tax_id', models.CharField(max_length=200, blank=True)),
                ('open_corp_id', models.CharField(max_length=200, blank=True)),
                ('vat_id', models.CharField(max_length=200, blank=True)),
                ('company_url', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'db_table': 'company_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'company_link_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('concession_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('concession_name', models.CharField(max_length=200)),
                ('unep_geo_id', models.CharField(max_length=200, blank=True)),
                ('country', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'concession_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConcessionLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'concession_link_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('country', models.CharField(max_length=200)),
                ('sign_date', models.CharField(max_length=200)),
                ('title_type', models.CharField(max_length=200, blank=True)),
                ('source_url', models.CharField(max_length=200)),
                ('doc_cloud_id', models.CharField(max_length=200)),
                ('doc_cloud_url', models.CharField(max_length=200)),
                ('sign_year', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contract_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContractLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'contract_link_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('host_url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'document_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('country', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'project_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'project_link_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('statement_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('statement_content', models.CharField(max_length=200)),
                ('definitive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'statement_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
