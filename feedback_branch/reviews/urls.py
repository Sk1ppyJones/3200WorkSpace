from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='index'),
    path('submit/', views.SubmissionView.as_view(), name='submit_review'),
    path('reviews/list/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='single_review')
]
