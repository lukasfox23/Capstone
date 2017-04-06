# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20170307_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='header_path',
            field=models.FileField(upload_to=b'headers/'),
        ),
    ]
