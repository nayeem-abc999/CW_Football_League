# Generated by Django 4.1.1 on 2022-12-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaguestat', '0005_alter_fixtures_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixtures',
            name='id',
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='matchID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
