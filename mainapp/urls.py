from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = 'home'),
   path('contact/', views.contact, name = 'contact'),
   path('contact/mail', views.contact_mail, name = "contact_mail"),
   path('social/', views.social, name="social"),
   path('upload/', views.file_upload, name = "file_upload")
]