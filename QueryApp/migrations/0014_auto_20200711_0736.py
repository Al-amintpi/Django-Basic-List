# Generated by Django 3.0.7 on 2020-07-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0013_auto_20200711_0722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='person',
            name='language',
            field=models.CharField(choices=[('en-us', 'English'), ('nl', 'Dutch')], default='en-us', max_length=5),
        ),
    ]
