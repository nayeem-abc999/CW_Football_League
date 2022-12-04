from django.db import models
from player.models import Player

class Team(models.Model): 
    teamID = models.PositiveIntegerField(unique=True)
    teamName = models.CharField(max_length=100,unique=True)
    managerName = models.CharField(max_length=100)
    teamSponsor = models.CharField(max_length=100)
    def __str__(self):
        return self.teamName

class TeamPlayers(models.Model):
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE )
    def __str__(self):
        return self.teamID.name