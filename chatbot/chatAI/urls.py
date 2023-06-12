from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path("chatbot", views.chatbot, name="chatbot"),
    path("chat", views.chat, name="chat"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]