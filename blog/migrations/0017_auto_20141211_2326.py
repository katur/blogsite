# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_uploaded', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('image', models.ImageField(upload_to=b'images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['is_published', '-time_published']},
        ),
    ]
