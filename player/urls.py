from django.urls import path
from . import views

urlpatterns = [
    #path to the all players page
    path('', views.show_players, name = 'show_players'),
    #path to the individual player details page
    path('<int:pID>/', views.player_details, name="player_details"),
    #path to the new player adding form
    path('newplayer/', views.new_player, name='new_player'),
    #path to the searching player by ID 
    path('search/', views.search_player, name='search_player')
    
]