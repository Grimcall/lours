from django.contrib import admin
from .models import *

admin.site.register(Content)
admin.site.register(TextContent)
admin.site.register(ImageContent)
admin.site.register(NoteContent)
admin.site.register(VideoContent)

# Register your models here.
