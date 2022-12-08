from django.core.management.base import BaseCommand
from team.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):

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

        TeamPlayers.objects.all().delete()
        
        tp1 = TeamPlayers(teamID = t1, player = p1)
        tp1.save()
        tp2 = TeamPlayers(teamID = t1, player = p2)
        tp2.save()
        tp3 = TeamPlayers(teamID = t1, player = p3)
        tp3.save()
        tp4 = TeamPlayers(teamID = t1, player = p4)
        tp4.save()
        tp5 = TeamPlayers(teamID = t1, player = p5)
        tp5.save()
        tp6 = TeamPlayers(teamID = t1, player = p6)
        tp6.save()
        tp7 = TeamPlayers(teamID = t1, player = p7)
        tp7.save()
        tp8 = TeamPlayers(teamID = t1, player = p8)
        tp8.save()
        tp9 = TeamPlayers(teamID = t1, player = p9)
        tp9.save()
        tp10 = TeamPlayers(teamID = t1, player = p10)
        tp10.save()
        tp11 = TeamPlayers(teamID = t1, player = p11)
        tp11.save()
       
      
    
        self.stdout.write('done2.') 