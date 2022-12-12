from django import forms
from .models import Player
from django.core.validators import MaxValueValidator, MinValueValidator 
# creating a form
class PlayerForm(forms.ModelForm):
    class Meta:
# Player model to be used
        model = Player
# labels to be used for the fields
        labels = {"pID": "Player ID", "fName" : "First Name",
            "lName" : "Surname", "height" : "Height (cm)", "weight" : "Weight (KG)",
            "position": "Position","num": "Jersey Number"}
# fields to be used
        fields = [
            "pID",
            "fName",
            "lName",
            "height",
            "weight",
            "position",
            "num"
        ]

# player searching using Player's ID form
class SearchDetailsForm(forms.Form):
    ID = forms.IntegerField(validators=[MinValueValidator(1000)])