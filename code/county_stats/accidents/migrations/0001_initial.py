# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('area_code', models.CharField(max_length=3)),
                ('descriptio', models.CharField(max_length=50)),
                ('file_name', models.CharField(max_length=50)),
                ('number', models.FloatField()),
                ('number0', models.FloatField()),
                ('polygon_id', models.IntegerField()),
                ('unit_id', models.IntegerField()),
                ('code', models.CharField(max_length=9)),
                ('hectares', models.FloatField()),
                ('area', models.FloatField()),
                ('type_code', models.CharField(max_length=2)),
                ('descript0', models.CharField(max_length=25)),
                ('type_cod0', models.CharField(null=True, max_length=3)),
                ('descript1', models.CharField(null=True, max_length=25)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=27700)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
