# Generated by Django 3.0.7 on 2020-07-11 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0014_auto_20200711_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='language',
        ),
    ]
