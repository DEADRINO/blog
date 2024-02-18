from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('personal_feed/', views.personal_feed, name='personal_feed'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/follow/',
         views.profile_follow,
         name='profile_follow'),
    path('profile/<str:username>/unfollow/',
         views.profile_unfollow,
         name='profile_unfollow'),

]