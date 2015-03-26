# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hulk.models


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0004_auto_20150326_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cik',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='jurisdiction',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='sic',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(max_length=200, primary_key=True, default=hulk.models.random_id, serialize=False),
            preserve_default=True,
        ),
    ]
