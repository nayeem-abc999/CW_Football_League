# Generated by Django 4.1.1 on 2022-12-04 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalMatch', models.PositiveIntegerField(default=0)),
                ('won', models.PositiveIntegerField(default=0)),
                ('lost', models.PositiveIntegerField(default=0)),
                ('drawn', models.PositiveIntegerField(default=0)),
                ('gf', models.PositiveIntegerField(default=0)),
                ('ga', models.PositiveIntegerField(default=0)),
                ('gd', models.PositiveIntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('teamName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]