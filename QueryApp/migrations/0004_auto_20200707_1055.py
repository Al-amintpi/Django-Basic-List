# Generated by Django 3.0.7 on 2020-07-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0003_person_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
