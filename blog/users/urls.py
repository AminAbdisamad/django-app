from django.urls import path
# Import views for login and logout
from django.contrib.auth import views as auth_views
from . import views as user_views
urlpatterns = [
    path('', user_views.login, name="login"),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
]
