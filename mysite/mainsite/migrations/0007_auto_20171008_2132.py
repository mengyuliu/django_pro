# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20171008_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='size_3',
        ),
    ]
