
from team.forms import TeamMemberForm
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
        return redirect(show_teams)
    context['form']= form
    return render(request, "team/signing.html",context)