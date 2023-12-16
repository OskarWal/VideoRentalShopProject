# Generated by Django 4.0.1 on 2022-01-27 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_movie_minimum_age_userprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='minimum_age',
            field=models.IntegerField(choices=[(0, 'Brak'), (7, 'Od 7 roku życia'), (18, 'Od 18 roku życia')], default=0),
        ),
        migrations.AlterField(
            model_name='movierented',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 11, 7, 38, 645366)),
        ),
    ]
