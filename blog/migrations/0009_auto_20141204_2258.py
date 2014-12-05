# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20141204_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postview',
            old_name='session',
            new_name='session_key',
        ),
        migrations.AlterField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 3, 58, 33, 94298, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
