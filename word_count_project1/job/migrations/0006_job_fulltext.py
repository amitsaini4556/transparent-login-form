# Generated by Django 2.2.10 on 2020-02-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_topwords'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='fulltext',
            field=models.TextField(default='000000'),
        ),
    ]
