from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_players, name = 'show_players'),
    path('newplayer', views.new_player, name='new_player')
]