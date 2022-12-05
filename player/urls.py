from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_players, name = 'show_players'),
    path('<int:pID>/', views.player_details, name="player_details"),
    path('newplayer/', views.new_player, name='new_player'),
    path('searchplayer/', views.search_player, name='search_player')
    
]