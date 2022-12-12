from django import forms
from .models import Player, TeamPlayers
from django.core.validators import MaxValueValidator, MinValueValidator 
class TeamMemberForm(forms.ModelForm):
    class Meta:
# TeamPlayers model to be used
        model = TeamPlayers
# fields to be used
        fields = [
            "teamID",
            "player"
        ]
# @teamID used to determine searched team
class SearchTeamForm(forms.Form):
    teamID = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])