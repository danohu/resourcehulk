# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pg.models.fields.datetime_
import hulk.models


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0008_auto_20150326_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='concession',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='doc',
            field=models.ForeignKey(blank=True, to='hulk.Document', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
        #migrations.AddField(
        #    model_name='document',
        #    name='source_url',
        #    field=models.CharField(default=b'', max_length=200),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='project',
        #    name='project_name',
        #    field=models.CharField(max_length=200, null=True, blank=True),
        #    preserve_default=True,
        #),
        migrations.AddField(
            model_name='project',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
        #migrations.AddField(
        #    model_name='statement',
        #    name='companies',
        #    field=models.ManyToManyField(to='hulk.Company', db_table=b'company_link_table', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='statement',
        #    name='concessions',
        #    field=models.ManyToManyField(to='hulk.Concession', db_table=b'concession_link_table', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='statement',
        #    name='contracts',
        #    field=models.ManyToManyField(to='hulk.Contract', db_table=b'contract_link_table', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='statement',
        #    name='doc',
        #    field=models.ForeignKey(default=None, to='hulk.Document'),
        #    preserve_default=False,
        #),
        #migrations.AddField(
        #    model_name='statement',
        #    name='projects',
        #    field=models.ManyToManyField(to='hulk.Project', db_table=b'project_link_table', blank=True),
        #    preserve_default=True,
        #),
        migrations.AddField(
            model_name='statement',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commodity',
            name='commodity_id',
            field=models.CharField(default=hulk.models.random_id, max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyalias',
            name='company_alias',
            field=models.CharField(default=hulk.models.random_id, max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='djangomigrations',
            name='applied',
            field=django_pg.models.fields.datetime_.DateTimeField(),
            preserve_default=True,
        ),
        #migrations.AlterField(
        #    model_name='document',
        #    name='doc_id',
        #    field=models.CharField(default=hulk.models.random_id, max_length=200, serialize=False, primary_key=True),
        #    preserve_default=True,
        #),
        migrations.AlterField(
            model_name='document',
            name='host_url',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default=hulk.models.random_id, max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statement',
            name='statement_id',
            field=models.CharField(default=hulk.models.random_id, max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
