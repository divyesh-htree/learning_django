# Generated by Django 4.2.4 on 2024-02-05 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 7, 1, 57, 431323, tzinfo=datetime.timezone.utc)),
        ),
    ]
