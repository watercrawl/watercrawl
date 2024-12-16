# Generated by Django 5.1.4 on 2024-12-15 22:47

import core.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlRequest',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(max_length=255, verbose_name='url')),
                ('status', models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('paused', 'Paused'), ('finished', 'Finished'), ('cancelling', 'Canceling'), ('canceled', 'Canceled'), ('failed', 'Failed')], default='new', max_length=255, verbose_name='status')),
                ('options', models.JSONField(default=dict, verbose_name='options')),
            ],
            options={
                'verbose_name': 'Crawl Request',
                'verbose_name_plural': 'Crawl Requests',
            },
        ),
        migrations.CreateModel(
            name='CrawlResult',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(max_length=255, verbose_name='url')),
                ('result', models.FileField(upload_to=core.utils.generate_crawl_result_file_path, verbose_name='result')),
            ],
            options={
                'verbose_name': 'Crawl Result',
                'verbose_name_plural': 'Crawl Results',
            },
        ),
    ]
