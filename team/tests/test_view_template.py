from django.test import TestCase
from player.models import Player
from team.models import Team, TeamPlayers
from django.urls import reverse
from django.db import transaction
from django.db.backends.sqlite3.base import IntegrityError
from django.db.utils import IntegrityError

class PlayerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        t1 = Team(teamID = 1, teamName = "United Comp Science", managerName = "Peter Ward", teamSponsor="Adidas" )
        t1.save()
        t2 = Team(teamID = 2, teamName = "FC Electronic Eng. ", managerName = "Jeremy Turner", teamSponsor="Nike" )
        t2.save()
        
    #testing all teams page
    def test_show_teams(self):
        response = self.client.get(reverse("show_teams"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "team/show_teams.html")
    
    #testing individual team's page
    def test_team_details(self):
        response = self.client.post(reverse("team_details",args=[2]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "team/team_details.html")

    #testing signing player
    def test_signing(self):
        p1 = Player(pID = 1000, fName = "Phil" , lName = "Smith", height = 156, weight = 60.5, num = 10, position = "Forward")
        p1.save()
        p2 = Player(pID = 1001, fName = "Jude" , lName = "Evans", height = 168, weight = 67.5, num = 9, position = "Forward")
        p2.save() 
        t1 = Team.objects.get(teamID = 1)
        data1 = {"teamID" : t1, "player" :p1 }
        response1 = self.client.post(reverse('signing'),data=data1)
        self.assertContains(response1, "10")
        self.assertContains(response1, "Phil")
        self.assertContains(response1, "Smith")

    #testing searching team details form and page
    def test_search_team(self): 
        response = self.client.post(reverse("search_team"))
        self.assertTemplateUsed(response, "team/search_team.html")


