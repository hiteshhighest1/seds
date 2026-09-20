from django.shortcuts import render, redirect
from django.contrib import messages

def index_view(request):
    return render(request, 'core/index.html')

def gallery_view(request):
    return render(request, 'core/gallery.html')

def team_view(request):
    return render(request, 'core/team.html')

def magazine_view(request):
    return render(request, 'core/magazine.html')

def contact_view(request):
    return render(request, 'core/contact.html')