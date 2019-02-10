from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="user-login"),
    path('register/', views.register, name="register")
]
