# Generated by Django 2.1.7 on 2019-03-18 04:09

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('boke', '0004_auto_20190318_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wenzhang',
            name='neirong',
            field=tinymce.models.HTMLField(verbose_name='内容1'),
        ),
    ]
