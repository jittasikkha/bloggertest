# Generated by Django 4.0.6 on 2022-09-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0009_remove_coverpic_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverpic',
            name='slide',
            field=models.BooleanField(default=False),
        ),
    ]
