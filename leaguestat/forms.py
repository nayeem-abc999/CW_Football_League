from django import forms
from .models import Fixtures

class MatchUpdateForm(forms.ModelForm):
    class Meta:
# Fixtures model to be used
        model = Fixtures
#labels to be used for the fields       
        labels = {"teamA": "Team A","teamB": "Team B",
        "goalA" :"Goal A", "goalB" :"Goal B"}
#fields to be used
        fields = [
           "teamA",
           "goalA",
           "teamB",
           "goalB"
        ]
        