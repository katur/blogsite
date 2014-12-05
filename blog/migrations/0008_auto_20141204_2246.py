# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20141204_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField()),
                ('session', models.CharField(max_length=50)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_published']},
        ),
        migrations.AlterField(
            model_name='post',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='time_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 5, 3, 46, 41, 594707, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
