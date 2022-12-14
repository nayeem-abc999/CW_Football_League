# Generated by Django 4.1.1 on 2022-12-04 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('leaguestat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchID', models.PositiveIntegerField(unique=True)),
                ('goalA', models.PositiveIntegerField(default=0)),
                ('goalB', models.PositiveIntegerField(default=0)),
                ('teamA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A', to='team.team')),
                ('teamB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B', to='team.team')),
            ],
        ),
    ]
