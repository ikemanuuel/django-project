from django.urls import path
from .views import ResidentsListCreateView, ResidentsListView, ResidentsDelete

urlpatterns = [
    path('residents/', ResidentsListCreateView.as_view(), name='residents-list-create'),
    path('residents/list', ResidentsListView.as_view(), name='residents-list'),
    path('residents/delete/<int:resident_id>/',
         ResidentsDelete.as_view(), name='property-delete'),
]
