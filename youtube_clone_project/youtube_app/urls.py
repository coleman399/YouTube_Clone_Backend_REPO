from django.urls import path
from . import views

urlpatterns = [
    path('youtube_app/', views.VideoList.as_view()),
    path('youtube_app/<str:pk>/', views.VideoDetails.as_view()),
]
