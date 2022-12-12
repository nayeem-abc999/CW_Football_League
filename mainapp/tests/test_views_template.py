from django.urls import reverse
from django.test import TestCase

class MainappTests(TestCase):
    @classmethod
    def setUpTestData(cls):
       pass
       
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "mainapp/home.html")
    
    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "mainapp/contact.html")
    
    def test_contact_mail(self):
        response = self.client.get(reverse('contact_mail'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "mainapp/contact_mail.html")
        self.assertContains(response,"Please enter your details and message:")
    
    def test_social(self):
        response = self.client.get(reverse('social'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "mainapp/social.html")

    def test_uplaod_file(self):
        response = self.client.get(reverse('file_upload'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "mainapp/upload_file.html")
        self.assertContains(response,"Write your details and upload the file here")

