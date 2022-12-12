from django import forms

"""
Form ContactForm
@name, for sender's name
@email, for valid email address
@subject, for email's subject
@message, message that needs to be sent
"""
class ContactForm(forms.Form):
    name = forms.CharField(label ="Name",required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    email = forms.EmailField(label = "E-mail",required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    subject = forms.CharField(label = "Subject",required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    message = forms.CharField(label = "Message",widget=forms.Textarea(attrs={'class': 'formfield'}), required=True)

"""
Form UploadFileForm

@name, for uploaders name
@brief, for a short brief about the uplaoding file
@file, to handle uploaded file
"""
class UploadFileForm(forms.Form):  
    name = forms.CharField(label="Your name",max_length=50,widget=forms.TextInput(attrs={'class': 'formfield'}))  
    brief = forms.CharField(label="A short brief",widget=forms.TextInput(attrs={'class': 'formfield'})) 
    file = forms.FileField() 