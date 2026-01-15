from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="hello-world"),
    path('hello/<str:name>',views.greeting_view,name='dynamic-hello'),
    path('square/<int:num>', views.square_view, name="squares")
]
