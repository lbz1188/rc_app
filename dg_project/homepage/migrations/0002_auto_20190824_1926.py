# Generated by Django 2.2.3 on 2019-08-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resort',
            name='banner_img',
            field=models.TextField(default='banner.jpg'),
        ),
        migrations.AddField(
            model_name='resort',
            name='img_dir',
            field=models.TextField(default='banner.jpg'),
        ),
        migrations.AddField(
            model_name='resort',
            name='target',
            field=models.CharField(default='/', max_length=100),
        ),
    ]
