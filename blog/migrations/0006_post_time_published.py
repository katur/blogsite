# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141205_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 2, 42, 38, 724454, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
