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
    #testing Player object creation
    def test_Player(self):
        db_count = Player.objects.all().count()
        p6 = Player(pID = 1005, fName = "David" , lName = "White", height = 144, weight = 67.5, num = 6, position = "Defender")
        p6.save()
        self.assertEqual(db_count + 1, 6)

    #testing invalid id using negative id number
    def test_invalid_negativeID(self):
        db_count = Player.objects.all().count()
        p = Player(pID = -1, fName = "Phil" , lName = "Smith", height = 156, weight = 60.5, num = 10, position = "Forward")
        
        try:
            with transaction.atomic():
                p.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count + 1, Player.objects.all().count())
    #testing invalid id using duplicate ID
    def test_invalid_duplicateID(self):
        db_count = Player.objects.all().count()
        p = Player(pID = 1001, fName = "James" , lName = "Smith", height = 156, weight = 70, num = 10, position = "Forward")
        try:
            with transaction.atomic():
                p.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count + 1, Player.objects.all().count())

    #testing adding new player using user's data
    def test_new_player_added(self):
        db_count = Player.objects.all().count()
        data = {"pID": 1006, "fName": "James", "lName": "Anderson", "height": 170, "weight" : 78, "num": 11, "position" :"Goal Keeper"}
        response = self.client.post(reverse('new_player'),data=data)
        self.assertEqual(Player.objects.count(), db_count+1)
