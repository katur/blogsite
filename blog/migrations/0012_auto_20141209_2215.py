# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('blog', '0011_auto_20141205_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time_modified',
            new_name='modified',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time_published',
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 3, 15, 19, 819245, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
