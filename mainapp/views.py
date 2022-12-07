from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm, UploadFileForm


from django.http import HttpResponse  
from mainapp.functions.functions import handle_uploaded_file  


def home(request):
    context = {}
    return render(request, "mainapp/home.html",context)

def contact(request):
    context = {}
    return render(request, "mainapp/contact.html",context)

def contact_mail(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = name + ':\n' + form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['in00199@surrey.ac.uk'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect(reverse('contact'))
    return render(request, 'mainapp/contact_mail.html', {"form": form})

def social(request):
    context = {}
    return render(request, "mainapp/social.html",context)


def file_upload(request):
    if request.method == 'POST':  
        uf = UploadFileForm(request.POST, request.FILES)  
        if uf.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        uf= UploadFileForm()  
        return render(request, "mainapp/upload_file.html", {'form': uf})   
