# Generated by Django 4.0.6 on 2022-09-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0008_alter_tags_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
