# Generated by Django 4.0.6 on 2022-09-25 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0010_coverpic_slide'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coverpic',
            options={'ordering': ('-created',)},
        ),
        migrations.RemoveField(
            model_name='coverpic',
            name='vdolink',
        ),
        migrations.AddField(
            model_name='coverpic',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]