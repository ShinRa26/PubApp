# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publist', '0003_pub_fromapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
