from django.urls import path
from . import views

urlpatterns = [
    #path for the league's current table 
    path('', views.league_table, name="league_table"),
    #path for the match result updating page
    path('matchresult', views.match_result, name="match_result"),
    #path to the season's all match results
    path('seasonhistory', views.season_history, name="season_history"),
    ]