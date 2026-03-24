from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SessionHomeView.as_view(), name='home'),
    path('change-color/', views.CHangeColorView.as_view(), name='change_color'),
    path('add-task/', views.AddTaskView.as_view(), name='add_task'),
    path('delete-task/<int:task_index>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('reset-session/', views.ResetSessionView.as_view(), name='reset_session'),
]
