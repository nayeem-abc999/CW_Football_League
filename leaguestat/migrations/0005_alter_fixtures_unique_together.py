# Generated by Django 4.1.1 on 2022-12-08 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaguestat', '0004_alter_fixtures_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fixtures',
            unique_together=set(),
        ),
    ]
