# Generated by Django 3.0.7 on 2020-06-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0012_auto_20200622_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photoupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='fileupload',
        ),
    ]
