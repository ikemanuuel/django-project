
from django.contrib import admin
from django.urls import path, include
from .views import activate_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('activation/<uidb64>/<token>/',
         activate_account, name='activate_account'),
]
