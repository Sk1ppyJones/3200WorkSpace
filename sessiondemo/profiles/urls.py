from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateProfileView.as_view(), name='create_profile'),
    path('success', views.SuccessView.as_view(), name='success'),
    path('profiles', views.UserProfilesView.as_view(), name='user-profiles')
]