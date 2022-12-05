from django import forms
from .models import Player, TeamPlayers

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
    teamID = forms.IntegerField()