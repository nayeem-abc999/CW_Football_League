# Generated by Django 4.1.1 on 2022-12-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaguestat', '0008_alter_fixtures_matchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='matchID',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
