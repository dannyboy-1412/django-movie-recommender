# Generated by Django 4.0.7 on 2022-09-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
