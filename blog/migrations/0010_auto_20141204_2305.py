# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20141204_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='number_of_views',
        ),
        migrations.AlterField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 4, 5, 24, 204943, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
