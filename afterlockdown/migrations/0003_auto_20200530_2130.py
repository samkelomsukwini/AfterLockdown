# Generated by Django 3.0.6 on 2020-05-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afterlockdown', '0002_post_call_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=250),
        ),
    ]
