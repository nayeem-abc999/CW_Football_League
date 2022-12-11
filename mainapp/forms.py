from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'formfield'}), required=True)

class UploadFileForm(forms.Form):  
    name = forms.CharField(label="Your name",max_length=50)  
    brief = forms.CharField(label="A short brief", max_length = 50) 
    file = forms.FileField() 