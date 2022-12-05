
from player.forms import SearchDetailsForm
from team.forms import SearchTeamForm, TeamMemberForm
from team.models import Team, TeamPlayers
from django.shortcuts import render
from django.shortcuts import redirect

def show_teams(request):
    context = {}
    context["teams"] = Team.objects.all()
    return render(request, "team/show_teams.html",context)

def team_details(request, teamID):
    
    context ={}
    context["data"] = TeamPlayers.objects.filter(teamID__teamID = teamID)
  
    return render(request, "team/team_details.html",context)

def signing(request):
    context ={}
    form = TeamMemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        teamID = form.cleaned_data["teamID"]
        k = teamID.teamID
        return redirect(team_details, teamID = k)
    context['form']= form
    return render(request, "team/signing.html",context)

def search_team(request):
    context ={}
    form = SearchTeamForm(request.POST or None)
    if form.is_valid():
        teamID = form.cleaned_data["teamID"]
        return redirect(team_details, teamID = teamID)
    context['form']= form
    return render(request, "team/search_team.html",context)
    