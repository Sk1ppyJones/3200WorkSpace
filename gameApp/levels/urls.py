from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('levels/<int:level_num>', views.level_by_number),
    path('levels/<str:level_name>', views.level_details, name='level-name'),
]
