from django.urls import path, include
from .views import Dashboard

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('dashboard/', Dashboard.as_view(),
         name='dashboard'),
]