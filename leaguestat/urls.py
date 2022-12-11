from django.urls import path
from . import views

urlpatterns = [
    path('', views.league_table, name="league_table"),
    path('matchresult', views.match_result, name="match_result"),
    path('seasonhistory', views.season_history, name="season_history"),
    ]