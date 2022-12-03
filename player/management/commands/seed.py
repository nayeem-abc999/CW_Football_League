from django.core.management.base import BaseCommand
from player.models import *
class Command(BaseCommand):
    def handle(self, *args, **options):

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
        self.stdout.write('done.') 