# Generated by Django 4.1 on 2022-11-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recommand", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ost",
            name="acousticness",
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="cluster",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="danceability",
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="energy",
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="loudness",
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="tempo",
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name="ost",
            name="valence",
            field=models.FloatField(blank=True),
        ),
    ]