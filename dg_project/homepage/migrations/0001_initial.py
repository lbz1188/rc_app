# Generated by Django 2.2.4 on 2019-08-04 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('parameters', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=100)),
                ('benefit', models.CharField(max_length=100)),
                ('logo_dir', models.CharField(max_length=100)),
                ('descption', models.TextField()),
                ('date_update', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
