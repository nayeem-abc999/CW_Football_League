from django.db import models
from player.models import Player

"""
Model Team
Used for creating team instances

@teamID, for unique team ID
@teamName, for unique team name
@managerName, team's manager 
@teamSponsor, team's sponsor
__str__, for standard return type
"""
class Team(models.Model): 
    teamID = models.PositiveIntegerField(unique=True)
    teamName = models.CharField(max_length=100,unique=True)
    managerName = models.CharField(max_length=100)
    teamSponsor = models.CharField(max_length=100)
    def __str__(self):
        return self.teamName

"""
Model Team
Used for creating players signed by specific team

@teamID, team in which the player will be assigned
@player, player who will be assigned
__str__, for standard return type
"""
class TeamPlayers(models.Model):
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE )
    def __str__(self):
        return self.teamID.name