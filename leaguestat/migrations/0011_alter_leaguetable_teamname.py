# Generated by Django 4.1.1 on 2022-12-11 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('leaguestat', '0010_alter_leaguetable_teamname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaguetable',
            name='teamName',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
    ]