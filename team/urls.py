from django.urls import path
from . import views

urlpatterns = [
    #path to the all teams details
    path('', views.show_teams, name="show_teams"),
    #path to the team's all player details
    path('<int:teamID>/', views.team_details, name="team_details"),
    #path to the new signing player page
    path('signing/', views.signing, name="signing"),
    #path to the team's all player details
    path('searchteam/', views.search_team, name="search_team")
    

]