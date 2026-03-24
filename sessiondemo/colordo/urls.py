from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SessionHomeView.as_view(), name='home'),
    path('change-color/', views.CHangeColorView.as_view(), name='change_color'),
]
