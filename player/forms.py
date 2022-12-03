from django import forms
from .models import Player
# creating a form
class PlayerForm(forms.ModelForm):
# create meta class
    class Meta:
# specify model to be used
        model = Player
# specify fields to be used
        fields = [
            "pID",
            "fName",
            "lName",
            "height",
            "weight",
            "num"
        ]