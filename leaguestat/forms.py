from django import forms
from .models import Fixtures
# creating a form
class MatchUpdateForm(forms.ModelForm):
# create meta class
    class Meta:
# specify model to be used
        model = Fixtures
# specify fields to be used
        fields = [
           "teamA",
           "teamB",
           "goalA",
           "goalB"
        ]