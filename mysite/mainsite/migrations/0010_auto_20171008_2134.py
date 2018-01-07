# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_auto_20171008_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size_3',
            new_name='size',
        ),
    ]
