from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="start"),
    path('posts', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.post_detail.as_view(), name='post-details'),
    path('read-later', views.read_later.as_view(), name='read-later'),
    path('create-post', views.post_create.as_view(), name='create-post'),    
]

