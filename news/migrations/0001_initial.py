# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(db_index=True, verbose_name='网址', max_length=256)),
                ('context', models.TextField(verbose_name='内容', blank=True, default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('author', models.ForeignKey(null=True, verbose_name='作者', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(db_index=True, verbose_name='栏目网站', max_length=256)),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
            ],
            options={
                'verbose_name_plural': '栏目',
                'verbose_name': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(verbose_name='归属栏目', to='news.Column'),
        ),
    ]
