# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20170320_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='conference_end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='conference',
            name='conference_start',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
