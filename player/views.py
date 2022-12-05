from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render
from .models import Player
from django.shortcuts import redirect
from .forms import PlayerForm, SearchDetailsForm

def player_details(request,pID):
    context ={}
    context["data"] = Player.objects.filter( pID = pID)
    return render(request, "player/player_details.html",context)

def show_players(request):
    context = {}
    context["all_players"] = Player.objects.all()

    return render(request, "player/view_players.html",context)


def new_player(request):
    context ={}
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(show_players)
    context['form']= form
    return render(request, "player/new_player.html",context)

def search_player(request):
    context ={}
    form = SearchDetailsForm(request.POST or None)
    if form.is_valid():
        pID = form.cleaned_data["pID"]
        return redirect(player_details, pID = pID)
    context['form']= form
    return render(request, "player/search_player.html",context)
    
        