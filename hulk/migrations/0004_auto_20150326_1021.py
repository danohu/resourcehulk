# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hulk', '0003_search_searchresult'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='search',
            field=models.ForeignKey(related_name='results', to='hulk.Search'),
            preserve_default=True,
        ),
    ]
