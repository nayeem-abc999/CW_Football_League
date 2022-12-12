from django.urls import path
from . import views

urlpatterns = [
   #path for the home page
   path('', views.home, name = 'home'),
   #path for the contact page
   path('contact/', views.contact, name = 'contact'),
   #path for the mail page
   path('contact/mail', views.contact_mail, name = "contact_mail"),
   #path for the social page
   path('social/', views.social, name="social"),
   #path for the social upload page
   path('social/upload/', views.file_upload, name = "file_upload")
]