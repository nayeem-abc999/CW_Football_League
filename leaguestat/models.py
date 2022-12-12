from django.db import models
from team.models import Team
"""
Model LeagueTable
Used for storing league standing data

@teamName, team's name which must be unique
@totalMatch, number of matches played
@won, number of matches won
@lost, number of matches lost
@drawn, number of matches drawn
@gf, goal scored
@ga, goal conceded
@gd, gd=gf-ga
@points, total points
"""
class LeagueTable(models.Model):
    teamName = models.OneToOneField(Team, unique=True, on_delete=models.CASCADE)
    totalMatch = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    lost =models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    gf = models.PositiveIntegerField(default=0)
    ga = models.PositiveIntegerField(default=0)
    gd = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

"""
Model Fixtures
Used for storing,updating match result

@matchID, match number
@teamA, one team
@teamB, other team
@goalA, goal scored by teamA
@goalB, goal scored by teamB
"""

class Fixtures(models.Model):
    matchID = models.AutoField(primary_key= True, auto_created= True)
    teamA = models.ForeignKey(Team, on_delete=models.CASCADE ,related_name = "A")
    teamB = models.ForeignKey(Team, on_delete=models.CASCADE,related_name = "B")
    goalA = models.PositiveIntegerField(default=0)
    goalB = models.PositiveIntegerField(default=0)
