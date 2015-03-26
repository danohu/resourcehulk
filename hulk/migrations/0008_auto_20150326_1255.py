# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0007_auto_20150326_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={},
        ),
        migrations.AlterModelOptions(
            name='companyalias',
            options={},
        ),
        migrations.AlterModelOptions(
            name='concession',
            options={},
        ),
        migrations.AlterModelOptions(
            name='concessionalias',
            options={},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={},
        ),
        migrations.AlterModelOptions(
            name='djangomigrations',
            options={},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AlterModelOptions(
            name='statement',
            options={},
        ),
        migrations.AddField(
            model_name='search',
            name='source',
            field=models.ForeignKey(blank=True, to='hulk.SourceInfo', null=True),
            preserve_default=True,
        ),
    ]
