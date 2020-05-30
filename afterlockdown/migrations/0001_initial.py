# Generated by Django 3.0.6 on 2020-05-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=160)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
