# Generated by Django 3.0.7 on 2020-07-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QueryApp', '0012_auto_20200711_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_trailing', models.BooleanField(default=True)),
                ('language', models.CharField(choices=[('en-us', 'English'), ('nl', 'Dutch')], default='en-us', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='language',
        ),
    ]
