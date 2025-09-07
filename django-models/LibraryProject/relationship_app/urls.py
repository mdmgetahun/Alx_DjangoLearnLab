from django import views
from django.urls import path, include
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),


    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login"
),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout"
    ),
    path("register/", views.register, name="register"),
]



