from django import views
from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view

urlpatterns = [
    path("books/", list_books, name="list_books"),  
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  path("register/", views.register, name="register"),
    path("logout/", logout_view.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path("login/", login_view.as_view(template_name='relationship_app/login.html'), name="login"),
]

logout_view.as_view(template_name='relationship_app/logout.html'), login_view.as_view(template_name='relationship_app/login.html'),