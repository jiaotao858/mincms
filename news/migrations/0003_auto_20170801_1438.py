# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170801_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='context',
            new_name='content',
        ),
    ]
