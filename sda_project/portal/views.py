from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,  *args, **kwargs):
    return render(request, "home.html", {})

def calendar_view(request, *args, **kwargs):
    return render(request, "calendar.html", {})

def downloads_view(request, *args, **kwargs):
    return render(request, "downloads.html", {})

def training_view(request, *args, **kwargs):
    return render(request, "training.html", {})