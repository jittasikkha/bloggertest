# Generated by Django 4.0.6 on 2022-09-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_tags_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]