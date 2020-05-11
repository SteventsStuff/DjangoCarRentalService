from django.urls import path

from . import views
from .views import (
    CarRentalListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, CarMarkListView
)

urlpatterns = [
    path('', views.home, name='rental-home'),
    path('catalog/', CarRentalListView.as_view(), name='rental-catalog'),
    path('car/mark/<str:mark_title>', CarMarkListView.as_view(), name='car-mark'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car-delete'),
    path('car/new/', CarCreateView.as_view(), name='car-create'),
    path('about/', views.about, name='rental-about'),
]
