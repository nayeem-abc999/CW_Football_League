from django import forms
from .models import Player
# creating a form
class PlayerForm(forms.ModelForm):
# create meta class
    class Meta:
# specify model to be used
        model = Player
# specify fields to be used
        labels = {"pID": "Player ID", "fName" : "First Name",
            "lName" : "Sure Name", "height" : "Height (cm)", "weight" : "Weight (KG)",
            "position": "Position","num": "Jersey Number"}
        fields = [
            "pID",
            "fName",
            "lName",
            "height",
            "weight",
            "position",
            "num"
        ]
class SearchDetailsForm(forms.Form):
    pID = forms.IntegerField()