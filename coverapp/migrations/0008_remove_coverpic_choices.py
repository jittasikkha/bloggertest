# Generated by Django 4.0.6 on 2022-09-24 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0007_alter_coverpic_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverpic',
            name='choices',
        ),
    ]