# Generated by Django 3.1.5 on 2021-01-24 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0012_auto_20210124_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='start_time',
        ),
    ]
