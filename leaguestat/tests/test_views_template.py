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

    def test_league_table(self):
        response = self.client.get(reverse("league_table"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "leaguestat/league_table.html")
    

    def test_match_result(self):
        response = self.client.get(reverse("match_result"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "leaguestat/match_result.html")
    
    def test_season_history(self):
        response = self.client.get(reverse("match_result"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "leaguestat/match_result.html")
        