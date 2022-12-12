from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render
from .models import Player
from django.shortcuts import redirect
from .forms import PlayerForm, SearchDetailsForm
from django.contrib import messages

#defined to generate individual player's details
# @pID, player ID 
def player_details(request,pID):
    context ={}
    context["data"] = Player.objects.filter( pID = pID)
    return render(request, "player/player_details.html",context)

#defined to generate all players details page
def show_players(request):
    context = {}
    context["all_players"] = Player.objects.all()

    return render(request, "player/view_players.html",context)

# defined to generate form for new players and save that data as a new player
def new_player(request):
    context ={}
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(show_players)
    context['form']= form
    return render(request, "player/new_player.html",context)

# defined to generate form to search individual player and show details about the player
def search_player(request):
    context ={}
    form = SearchDetailsForm(request.POST or None)
    
    if form.is_valid():
        ID = form.cleaned_data["ID"]
        i = Player.objects.filter(pID=ID).exists()
        if i==True:
            return redirect(player_details, pID = ID)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Player ID')
            context['form']= form
            return render(request, "player/search_player.html",context)
    context['form']= form
    return render(request, "player/search_player.html",context)
    
        