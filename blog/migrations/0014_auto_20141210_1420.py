# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20141209_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_published']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='time_published',
        ),
    ]
