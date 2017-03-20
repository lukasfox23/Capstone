# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20170304_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file_path',
            field=models.FileField(upload_to=b'uploads/'),
        ),
    ]
