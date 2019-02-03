
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    # Create blog home page without redirect
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
