# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_uploadedimage_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedimage',
            old_name='author',
            new_name='user',
        ),
    ]
