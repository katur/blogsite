# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_time_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time_created',
        ),
        migrations.AlterField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
