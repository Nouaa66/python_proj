# Generated by Django 2.2.4 on 2021-04-29 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_auto_20210429_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish_granted',
            name='likes',
        ),
    ]
