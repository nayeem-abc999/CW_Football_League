from django.test import TestCase
from player.models import Player
from django.urls import reverse
from django.db import transaction
from django.db.backends.sqlite3.base import IntegrityError
from django.db.utils import IntegrityError

class PlayerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        p1 = Player(pID = 1000, fName = "Phil" , lName = "Smith", height = 156, weight = 60.5, num = 10, position = "Forward")
        p1.save()
        p2 = Player(pID = 1001, fName = "Jude" , lName = "Evans", height = 168, weight = 67.5, num = 9, position = "Forward")
        p2.save()
        p3 = Player(pID = 1002, fName = "Harry" , lName = "Walker", height = 176, weight = 68, num = 11, position = "Forward")
        p3.save()
        p4 = Player(pID = 1003, fName = "Jordan" , lName = "Wilson", height = 156, weight = 67.5, num = 7, position = "Defender")
        p4.save()
        p5 = Player(pID = 1004, fName = "Robert" , lName = "Smith", height = 177, weight = 60.5, num = 8, position = "Defender")
        p5.save()
    #testing all players details page
    def test_show_players(self):
        response = self.client.get(reverse("show_players"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "player/view_players.html")
    
    #testing individual player details page
    def test_player_details(self):
        response = self.client.post(reverse("player_details",args=[1003]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "player/player_details.html")

    #testing player searching page
    def test_search_player(self):
        response = self.client.post(reverse("search_player"))
        self.assertContains(response,"Enter Player ID")

    
    

