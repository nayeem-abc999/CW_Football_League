from django.db import models
from team.models import Team

class LeagueTable(models.Model):
    teamName = models.ForeignKey(Team, on_delete=models.CASCADE)
    totalMatch = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    lost =models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    gf = models.PositiveIntegerField(default=0)
    ga = models.PositiveIntegerField(default=0)
    gd = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

class Fixtures(models.Model):
    matchID = models.AutoField(primary_key= True, auto_created= True)
    teamA = models.ForeignKey(Team, on_delete=models.CASCADE ,related_name = "A")
    teamB = models.ForeignKey(Team, on_delete=models.CASCADE,related_name = "B")
    goalA = models.PositiveIntegerField(default=0)
    goalB = models.PositiveIntegerField(default=0)
