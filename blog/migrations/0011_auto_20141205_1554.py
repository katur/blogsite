# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20141204_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 20, 54, 2, 341383, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
