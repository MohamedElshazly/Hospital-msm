# Generated by Django 3.1.5 on 2021-01-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0011_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(max_length=255, null=True, verbose_name='Manufacturer'),
        ),
    ]