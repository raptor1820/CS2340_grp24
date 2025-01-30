from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, "GT_Movie/landing.html")

def about(request):
    return render(request, "GT_Movie/about.html")

def log_in(request):
    return render(request, "GT_Movie/logIn.html")

def sign_up(request):
    return render(request, "GT_Movie/sign_up.html")

