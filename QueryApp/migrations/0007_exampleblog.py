# Generated by Django 3.0.7 on 2020-06-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0006_auto_20200620_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
