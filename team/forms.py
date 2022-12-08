from django import forms
from .models import Player, TeamPlayers
from django.core.validators import MaxValueValidator, MinValueValidator 
class TeamMemberForm(forms.ModelForm):
# create meta class
    class Meta:
# specify model to be used
        model = TeamPlayers
# specify fields to be used
        fields = [
            "teamID",
            "player"
        ]
class SearchTeamForm(forms.Form):
    teamID = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])