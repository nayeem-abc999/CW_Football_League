from django.test import TestCase
from player.models import Player
from team.models import Team, TeamPlayers
from django.urls import reverse
from django.db import transaction
from django.db.backends.sqlite3.base import IntegrityError
from django.db.utils import IntegrityError

class TeamTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        t1 = Team(teamID = 1, teamName = "United Comp Science", managerName = "Peter Ward", teamSponsor="Adidas" )
        t1.save()
        t2 = Team(teamID = 2, teamName = "FC Electronic Eng. ", managerName = "Jeremy Turner", teamSponsor="Nike" )
        t2.save()
        t3 = Team(teamID = 3, teamName = "Team Mechanical", managerName = "Matt Clark", teamSponsor="Puma" )
        t3.save()
        t4 = Team(teamID = 4, teamName = "FC Civil", managerName = "Robin Baker", teamSponsor="Fly Emirates" )
        t4.save()
        t5 = Team(teamID = 5, teamName = "United Chemistry", managerName = "Austin Lee", teamSponsor="Ethihad Airways" )
        t5.save()
        p1 = Player(pID = 1000, fName = "Phil" , lName = "Smith", height = 156, weight = 60.5, num = 10, position = "Forward")
        p1.save()
        p2 = Player(pID = 1001, fName = "Jude" , lName = "Evans", height = 168, weight = 67.5, num = 9, position = "Forward")
        p2.save()
        p3 = Player(pID = 1002, fName = "Harry" , lName = "Walker", height = 176, weight = 68, num = 11, position = "Forward")
        p3.save()
       
    def test_team(self):
        total_teams = Team.objects.count()
        t6 = Team(teamID = 6, teamName = "FC Mathematics", managerName = "Arthur Parker", teamSponsor="Qatar Airways" )
        t6.save()

        self.assertEqual(total_teams + 1, 6)

    def test_invalid_duplicate_teamID(self):
        total_teams = Team.objects.all().count()
        t = Team(teamID = 5, teamName = "XYZ", managerName = "ABC", teamSponsor = "IDK")
        
        try:
            with transaction.atomic():
                t.save()
        except IntegrityError:
            pass
        self.assertNotEqual(total_teams + 1, Team.objects.all().count())
    
    def test_invalid_duplicate_teamName(self):
        total_teams = Team.objects.all().count()
        t = Team(teamID = 6, teamName = "Team Mechanical", managerName = "ABC", teamSponsor = "IDK")
        
        try:
            with transaction.atomic():
                t.save()
        except IntegrityError:
            pass
        self.assertNotEqual(total_teams + 1, Team.objects.all().count())

    def test_TeamPlayers(self):
       
        t1 = Team.objects.get(teamID = 1)
        p1 = Player.objects.get(pID = 1000)
        p2 = Player.objects.get(pID = 1001)
        p3 = Player.objects.get(pID = 1002)

        tp = TeamPlayers( teamID = t1,player = p1)
        tp.save()
        tp = TeamPlayers( teamID = t1,player = p2)
        tp.save()
        tp = TeamPlayers( teamID = t1,player = p3)
        tp.save()
               
        total = TeamPlayers.objects.filter(teamID__teamID=1).count()

        self.assertEqual(total, 3)
        

