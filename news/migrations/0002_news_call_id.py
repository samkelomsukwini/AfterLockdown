# Generated by Django 3.0.6 on 2020-05-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='call_id',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]