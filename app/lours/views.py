from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Content, TextContent, ImageContent, NoteContent, VideoContent
from lours.py_utils import bcolors

import json

ITEMS_PER_PAGE = 6
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    
    # Get all content items ordered by creation date
    all_content = Content.objects.filter(user=request.user).order_by('-created_at')
    
    # Set up pagination
    paginator = Paginator(all_content, ITEMS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    content_list = []
    
    # Process the items for the current page
    for item in page_obj:
        if item.content_type == 'text':
            text_content = TextContent.objects.get(content=item)
            content_list.append({
                'id': item.id,
                'title': item.title,
                'content_type': item.content_type,
                'textcontent': text_content.text,
                'created_at': item.created_at,
            })
        elif item.content_type == 'image':
            image_content = ImageContent.objects.get(content=item)
            content_list.append({
                'id': item.id,
                'title': item.title,
                'content_type': item.content_type,
                'imagecontent': image_content.image.url,
                'created_at': item.created_at,
            })
        elif item.content_type == 'note':
            note_content = NoteContent.objects.get(content=item)
            content_list.append({
                'id': item.id,
                'title': item.title,
                'content_type': item.content_type,
                'notecontent': note_content.text,
                'created_at': item.created_at,
            })
        elif item.content_type == 'video':
            video_content = VideoContent.objects.get(content=item)
            content_list.append({
                'id': item.id,
                'title': item.title,
                'content_type': item.content_type,
                'videocontent': video_content.video.url,
                'created_at': item.created_at,
            })
    
    # Split current page content into two columns
    MID_INDEX = len(content_list)//2
    if len(content_list) % 2 != 0:
        MID_INDEX += 1
    page1 = content_list[:MID_INDEX]
    page2 = content_list[MID_INDEX:]

    return render(request, '01Landing/00landing.html', {
        'content_list': content_list, 
        'page1': page1, 
        'page2': page2,
        'page_obj': page_obj,
    })

def auth(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(request, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print(bcolors.FAIL + "Invalid password" + bcolors.ENDC)
            return render(request, '02Auth/00auth.html', {'error': 'Invalid password'})
    return render(request, '02Auth/00auth.html')

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

@login_required
def get_content(request, content_id):
    """Get content details for editing"""
    content = get_object_or_404(Content, id=content_id, user=request.user)
    data = {
        'id': content.id,
        'title': content.title,
        'content_type': content.content_type,
        'created_at': content.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    if content.content_type == 'text':
        text_content = TextContent.objects.get(content=content)
        data['text'] = text_content.text
    elif content.content_type == 'note':
        note_content = NoteContent.objects.get(content=content)
        data['text'] = note_content.text
    elif content.content_type == 'image':
        image_content = ImageContent.objects.get(content=content)
        data['image_url'] = image_content.image.url
    elif content.content_type == 'video':
        video_content = VideoContent.objects.get(content=content)
        data['video_url'] = video_content.video.url
        
    return JsonResponse(data)

@login_required
def update_content(request, content_id):
    """Update existing content"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
        
    content = get_object_or_404(Content, id=content_id, user=request.user)
    content.title = request.POST.get('title', content.title)
    content.save()
    
    if content.content_type == 'text':
        text_content = TextContent.objects.get(content=content)
        text_content.text = request.POST.get('content', text_content.text)
        text_content.save()
    elif content.content_type == 'note':
        note_content = NoteContent.objects.get(content=content)
        note_content.text = request.POST.get('content', note_content.text)
        note_content.save()
    # Note: For image and video, we would handle file uploads here
    # But for simplicity, we're not implementing that right now
    
    return redirect('index')

@login_required
def delete_content(request, content_id):
    """Delete content"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
        
    content = get_object_or_404(Content, id=content_id, user=request.user)
    
    # Delete the content (will cascade delete related content)
    content.delete()
    
    return redirect('index')

def notes(request):
    return render(request, 'lours/notes.html')

def posts(request):
    return render(request, 'lours/posts.html')

def logout_view(request):
    logout(request)
    return redirect('auth')


