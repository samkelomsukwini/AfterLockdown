# Generated by Django 3.0.6 on 2020-05-30 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatingsystem',
            name='is_mobile',
        ),
    ]
