from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_teams, name="show_teams"),
    path('<int:teamID>/', views.team_details, name="team_details"),
    path('signing', views.signing, name="signing")
]