# Generated by Django 4.0.6 on 2022-07-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverpic',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]