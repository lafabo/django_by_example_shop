# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'db_tablespace': '',
                'db_table': 'shop_category_translation',
                'managed': True,
                'verbose_name': 'category Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_tablespace': '',
                'db_table': 'shop_product_translation',
                'managed': True,
                'verbose_name': 'product Translation',
                'default_permissions': (),
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories', 'verbose_name': 'category'},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([]),
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='master',
            field=models.ForeignKey(editable=False, to='shop.Product', related_name='translations', null=True),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='master',
            field=models.ForeignKey(editable=False, to='shop.Category', related_name='translations', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
