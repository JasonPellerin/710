# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dabber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dabber',
            name='dbr_pic',
            field=models.ImageField(upload_to=b'images/dabberthumbs/', blank=True),
            preserve_default=True,
        ),
    ]
