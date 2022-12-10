from django.core.management.base import BaseCommand
from leaguestat.models import Fixtures, LeagueTable
from team.models import *
from player.models import *
class Command(BaseCommand):
    def handle(self, *args, **options):

        LeagueTable.objects.all().delete()
        t1 = Team.objects.get(teamID = 1)
        t2 = Team.objects.get(teamID = 2)
        t3 = Team.objects.get(teamID = 3)
        t4 = Team.objects.get(teamID = 4)
        t5 = Team.objects.get(teamID = 5)
        lt1 = LeagueTable(teamName = t1, totalMatch = 0,won =0,lost = 0,drawn=0,gf = 0,ga =0,gd =0,points = 0)
        lt1.save()
        lt2 = LeagueTable(teamName = t2)
        lt2.save()
        lt3 = LeagueTable(teamName = t3)
        lt3.save()
        lt4 = LeagueTable(teamName = t4)
        lt4.save()
        lt5 = LeagueTable(teamName = t5)
        lt5.save()


        Fixtures.objects.all().delete()
        
        self.stdout.write('done3') 