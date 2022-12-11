from django import forms
from .models import Fixtures
# creating a form
class MatchUpdateForm(forms.ModelForm):
# create meta class
    class Meta:
# specify model to be used
        model = Fixtures
        
        labels = {"teamA": "Team A","teamB": "Team B",
        "goalA" :"Goal A", "goalB" :"Goal B"}
# specify fields to be used
        fields = [
           "teamA",
           "goalA",
           "teamB",
           "goalB"
        ]
        