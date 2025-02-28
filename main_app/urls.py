from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('feed/', views.feed, name='feed'),
    path('feed/<str:trend>', views.trend, name='trend'),
    path('feed/<str:trend>/<int:tweet_id>', views.tweet, name='tweet'),
]