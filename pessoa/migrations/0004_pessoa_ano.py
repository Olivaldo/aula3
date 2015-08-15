# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='ano',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
