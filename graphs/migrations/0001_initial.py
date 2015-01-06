# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import graphs.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('graph_type', models.CharField(max_length=10, verbose_name=b'Type: ', choices=[(b'line', b'Line'), (b'pie', b'Pie'), (b'hist', b'Histogram')])),
                ('csv_file', models.FileField(upload_to=graphs.models.get_upload_file_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
