from django.shortcuts import render
from django.shortcuts import redirect
from leaguestat.forms import MatchUpdateForm
from .models import Fixtures, LeagueTable
# Create your views here.
def league_table(request):
    context = {}
    context["table"] = LeagueTable.objects.all().order_by('-points')
    return render(request, "leaguestat/league_table.html",context)

def match_result(request):
    context = {}
    form = MatchUpdateForm(request.POST or None)
    if form.is_valid():
        form.save()
        teamA = form.cleaned_data.get('teamA')
        teamB = form.cleaned_data.get('teamB')
        goalA = form.cleaned_data.get('goalA')
        goalB = form.cleaned_data.get('goalB')
        tA = LeagueTable.objects.get(teamName__teamID=teamA.teamID)
        tB = LeagueTable.objects.get(teamName__teamID=teamB.teamID)
       
        tA.totalMatch =  tA.totalMatch + 1
        tB.totalMatch =  tB.totalMatch + 1

        tA.gf = tA.gf + goalA
        tB.gf = tB.gf + goalB

        tA.ga = tA.ga + goalB
        tB.ga = tB.ga + goalA

        tA.gd = tA.gf - tA.ga
        tB.gd = tB.gf - tB.ga

        if goalA == goalB:
            tA.drawn = tA.drawn + 1
            tB.drawn = tB.drawn + 1
            tA.points = tA.points + 1
            tB.points = tB.points + 1
        elif goalA > goalB:
            tA.won = tA.won + 1
            tB.lost =tB.lost + 1
            tA.points = tA.points + 3
        elif goalB > goalA:
            tB.won = tB.won + 1
            tA.lost =tA.lost + 1
            tB.points = tB.points + 3

        tA.save()
        tB.save()
        return redirect(season_history)

    context['form']= form
    return render(request, "leaguestat/match_result.html",context)

def season_history(request):
    context = {}
    context["season_history"] = Fixtures.objects.all().order_by('-matchID')
    return render(request, "leaguestat/season_history.html",context)