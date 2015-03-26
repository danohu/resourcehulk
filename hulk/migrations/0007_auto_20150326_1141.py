# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_pg.models.fields.datetime_
import django_pg.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0006_auto_20150326_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('contributor', models.CharField(max_length=200)),
                ('license', models.CharField(max_length=200)),
                ('date', django_pg.models.fields.datetime_.DateTimeField(default=datetime.datetime.now)),
                ('info', django_pg.models.fields.json.JSONField(default=b'{}', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='source',
            field=models.ForeignKey(related_name='companies', blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
    ]
