# Generated by Django 2.1.7 on 2019-03-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceshi1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]