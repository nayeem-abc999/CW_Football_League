from django.test import TestCase
from leaguestat.models import Fixtures, LeagueTable
from player.models import Player
from django.urls import reverse
from django.db import transaction
from django.db.backends.sqlite3.base import IntegrityError
from django.db.utils import IntegrityError
from team.models import Team

class LeagueTableTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.all().delete()
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
        t6 = Team(teamID = 6, teamName = "FC Mathematics", managerName = "Arthur Parker", teamSponsor="Qatar Airways" )
        t6.save()

        lt1 = LeagueTable(teamName = t1, totalMatch = 0,won =0,lost = 0,drawn=0,gf = 0,ga =0,gd =0,points = 0)
        lt1.save()
        lt2 = LeagueTable(teamName = t2)
        lt2.save()
        lt3 = LeagueTable(teamName = t3)
        lt3.save()
    #testing leagueTable data
    def test_LeagueTable_save(self):
        db_count = LeagueTable.objects.all().count()
        t4 = Team.objects.get(teamID=4)
        lt4 = LeagueTable(teamName = t4)
        lt4.save()
        self.assertEqual(db_count + 1, 4)
    
    #testing duplicate name in LeagueTable
    def test_duplicate_league_team(self):
        db_count = LeagueTable.objects.all().count()
        t2 = Team.objects.get(teamID=2)
        lt2 = LeagueTable(teamName = t2)
        try:
            with transaction.atomic():
                lt2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count + 1, LeagueTable.objects.all().count())
    
    
    


class FixturesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.all().delete()
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
        t6 = Team(teamID = 6, teamName = "FC Mathematics", managerName = "Arthur Parker", teamSponsor="Qatar Airways" )
        t6.save()

    
    def test_fixtures(self):
        
        t1 = Team.objects.get(teamID=1)
        t2 = Team.objects.get(teamID=2)
        t3 = Team.objects.get(teamID=3)

        f1 = Fixtures(teamA = t1, teamB = t2, goalA = 4, goalB =2)
        f1.save()
        f2 = Fixtures(teamA = t2, teamB = t3, goalA = 2, goalB =2)
        f2.save()
        total = Fixtures.objects.all().count()
        self.assertEqual(total,2)
