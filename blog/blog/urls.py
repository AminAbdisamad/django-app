
from django.contrib import admin
from django.urls import path, include
# Import views for login and logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('pages/', include('pages.urls')),
    # Create blog home page without redirect
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]
