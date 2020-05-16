from django.urls import path

from . import views
from .views import (
    CarRentalListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, CarMarkListView,
    CarMarkCreateView, CarConditionCreateView, CarClassCreateView,
    DriversListView, DriverDetailView, DriverCreateView, DriverUpdateView, DriverDeleteView
)

urlpatterns = [
    # general
    path('', views.home, name='rental-home'),
    path('about/', views.about, name='rental-about'),
    # cars
    path('car-catalog/', CarRentalListView.as_view(), name='car-catalog'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car-delete'),
    path('car/new/', CarCreateView.as_view(), name='car-create'),
    # edit car marks
    path('car-mark/new/', CarMarkCreateView.as_view(), name='car-mark-create'),
    # edit car condition
    path('car-condition/new/', CarConditionCreateView.as_view(), name='car-condition-create'),
    # edit car class
    path('car-class/new/', CarClassCreateView.as_view(), name='car-class-create'),
    # cars: filters
    path('car/mark/<str:mark_title>', CarMarkListView.as_view(), name='car-mark'),
    # drivers
    path('driver-catalog/', DriversListView.as_view(), name='driver-catalog'),
    path('driver/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    path('driver/create/', DriverCreateView.as_view(), name='driver-create'),
    path('driver/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver-delete'),
    path('driver/<int:pk>/update/', DriverUpdateView.as_view(), name='driver-update'),
]


