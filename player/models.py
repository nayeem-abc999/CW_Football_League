from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


"""
Model Player
Used for creating team instances

@pID, for unique player's ID
@fName, player's first name
@lName, player's last/surname name
@height, player's height with constraints
@weight, player's weight with constraints
@num, player's jersey number
@position, player's role in the team

__str__, for standard return type
"""

class Player(models.Model): 
    pID = models.PositiveIntegerField(unique=True,validators=[MinValueValidator(1000)])
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(120)])
    weight = models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(50)])
    num = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    position = models.CharField(max_length=20, default="Unsigned")
    
    def __str__(self):
        s = str(self.pID) 
        return s +" " + self.fName + " " + self.lName