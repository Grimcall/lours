from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('note', 'Note'),
        ('video', 'Video'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TextContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.TextField()

class ImageContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

class NoteContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.TextField()

#class AudioContent(models.Model):
#    content = models.ForeignKey(Content, on_delete=models.CASCADE)
#    audio = models.FileField(upload_to='audios/')

class VideoContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
