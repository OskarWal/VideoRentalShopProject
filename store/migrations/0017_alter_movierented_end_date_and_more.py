# Generated by Django 4.0.1 on 2022-01-27 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_movie_minimum_age_alter_movierented_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierented',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 11, 13, 36, 561702)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 27, 11, 13, 36, 561701)),
        ),
    ]
