from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, '01Landing/00landing.html')

def landing(request):
    return render(request, 'lours/landing.html')

def auth(request):
    return render(request, 'lours/auth.html')

def notes(request):
    return render(request, 'lours/notes.html')

def posts(request):
    return render(request, 'lours/posts.html')


