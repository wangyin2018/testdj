# Generated by Django 2.1.7 on 2019-03-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boke', '0002_auto_20190315_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wenzhang',
            name='img',
            field=models.ImageField(upload_to='img/%Y%m%d', verbose_name='图片路径'),
        ),
    ]
