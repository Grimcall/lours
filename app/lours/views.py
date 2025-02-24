from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Content, TextContent, ImageContent, NoteContent, VideoContent

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    return render(request, '01Landing/00landing.html')

def auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, '02Auth/00auth.html', {'form': form})

@login_required
def create_text(request):
    if request.method == 'POST':
        content = Content.objects.create(
            user=request.user,
            title=request.POST['title'],
            content_type='text'
        )
        TextContent.objects.create(
            content=content,
            text=request.POST['content']
        )
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def create_image(request):
    if request.method == 'POST':
        content = Content.objects.create(
            user=request.user,
            title=request.POST['title'],
            content_type='image'
        )
        ImageContent.objects.create(
            content=content,
            image=request.FILES['image']
        )
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def create_note(request):
    if request.method == 'POST':
        content = Content.objects.create(
            user=request.user,
            title=request.POST['title'],
            content_type='note'
        )
        NoteContent.objects.create(
            content=content,
            text=request.POST['content']
        )
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def create_video(request):
    if request.method == 'POST':
        content = Content.objects.create(
            user=request.user,
            title=request.POST['title'],
            content_type='video'
        )
        VideoContent.objects.create(
            content=content,
            video=request.FILES['video']
        )
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def notes(request):
    return render(request, 'lours/notes.html')

def posts(request):
    return render(request, 'lours/posts.html')


