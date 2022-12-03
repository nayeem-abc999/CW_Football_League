from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Player
from django.shortcuts import redirect
from .forms import PlayerForm

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