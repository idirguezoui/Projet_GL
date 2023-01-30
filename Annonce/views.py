from django.shortcuts import render
from Annonce.models import adresseForm,Profiles
from django.contrib.auth.models import User

# Create your views here.

def sign_in(request):
    return render(request, 'sign_in.html')

def firstPage(request):
    return render(request, 'first_page.html')

def sign_up(request):
    adresse = adresseForm()
    if request.method=='POST':
        print(request.POST)
    return render(request, 'sign_up.html', {'adresse':adresse})