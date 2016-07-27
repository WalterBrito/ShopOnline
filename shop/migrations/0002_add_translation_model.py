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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'shop_category_translation',
                'verbose_name': 'category Translation',
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'shop_product_translation',
                'verbose_name': 'product Translation',
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
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
            field=models.ForeignKey(related_name='translations', null=True, editable=False, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', null=True, editable=False, to='shop.Category'),
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
