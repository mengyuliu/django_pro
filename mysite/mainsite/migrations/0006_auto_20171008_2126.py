# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20171005_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small1'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
