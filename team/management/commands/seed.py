from django.core.management.base import BaseCommand
from team.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):

        Team.objects.all().delete()
        t1 = Team(teamID = 1, teamName = "CS", managerName = "saif", teamSponsor="Adidas" )
        t1.save()
        t2 = Team(teamID = 2, teamName = "EEE", managerName = "Nafis", teamSponsor="Adidas" )
        t2.save()
        t3 = Team(teamID = 3, teamName = "Math", managerName = "Matt", teamSponsor="Adidas" )
        t3.save()
        t4 = Team(teamID = 4, teamName = "Chemistry", managerName = "Boris", teamSponsor="Adidas" )
        t4.save()
        t5 = Team(teamID = 5, teamName = "Physics", managerName = "Jay", teamSponsor="Adidas" )
        t5.save()

        Player.objects.all().delete()

        p1 = Player(pID = 1000, fName = "Islam" , lName = "Nayeemul", height = 156, weight = 60.5, num = 10)
        p1.save()
        p2 = Player(pID = 1001, fName = "Syed" , lName = "Ismead", height =145.47 , weight = 65, num =11 )
        p2.save()
        p3 = Player(pID = 1002, fName = "James" , lName = "Block", height = 178.39, weight = 70.8, num = 12)
        p3.save()
        p4 = Player(pID = 1003, fName = "George" , lName = "Washington", height = 166, weight =78 , num = 13)
        p4.save()
        p5 = Player(pID = 1004, fName = "Barak" , lName = "Feen", height =155.44 , weight = 66, num =14 )
        p5.save()
        
        TeamPlayers.objects.all().delete()
        
        tp = TeamPlayers(teamID = t1, player = p1)
        tp.save()
        tp = TeamPlayers(teamID = t1, player = p2)
        tp.save()
        tp = TeamPlayers(teamID = t2, player = p3)
        tp.save()
        tp = TeamPlayers(teamID = t2, player = p4)
        tp.save()
        tp = TeamPlayers(teamID = t2, player = p5)
        tp.save()
       
      
    
        self.stdout.write('done2.') 