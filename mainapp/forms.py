from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UploadFileForm(forms.Form):  
    name = forms.CharField(label="Your name",max_length=50)  
    brief = forms.CharField(label="A short brief", max_length = 50) 
    file = forms.FileField() # for creating file input  