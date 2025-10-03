from django.urls import path, include
from .views import UserLoginView, RegisterView, UserLogoutView, home_view, posts_view,  ProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('posts/', posts_view, name='posts'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]