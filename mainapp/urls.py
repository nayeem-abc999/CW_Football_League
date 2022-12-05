from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = 'home'),
   path('contact/', views.contact, name = 'contact'),
   path('contact/mail', views.contact_mail, name = "contact_mail")
]