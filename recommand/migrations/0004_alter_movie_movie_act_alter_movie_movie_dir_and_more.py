# Generated by Django 4.1 on 2022-11-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommand", "0003_alter_ost_acousticness_alter_ost_danceability_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="movie_act",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="movie",
            name="movie_dir",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="movie",
            name="movie_ger",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="movie",
            name="movie_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="ost",
            name="ost_name",
            field=models.CharField(max_length=200),
        ),
    ]
