from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('notes/', views.notes, name='notes'),
    path('posts/', views.posts, name='posts'),
    path('create/text/', views.create_text, name='create_text'),
    path('create/image/', views.create_image, name='create_image'),
    path('create/note/', views.create_note, name='create_note'),
    path('create/video/', views.create_video, name='create_video'),
    path('content/<int:content_id>/', views.get_content, name='get_content'),
    path('content/<int:content_id>/update/', views.update_content, name='update_content'),
    path('content/<int:content_id>/delete/', views.delete_content, name='delete_content'),
    path('logout/', views.logout_view, name='logout'),
]
