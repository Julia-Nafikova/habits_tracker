from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include('tracker.urls'), name='tracker'),
    path('users/', include('users.urls'), name='users'),
]
