# Generated by Django 4.0.1 on 2022-01-25 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_movie_language_alter_movierented_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='soundtrack',
            field=models.CharField(choices=[('Lector', 'Lektor'), ('Original', 'Oryginalna'), ('Dubbing', 'Dubbing')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movierented',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 10, 33, 13, 504463)),
        ),
    ]
