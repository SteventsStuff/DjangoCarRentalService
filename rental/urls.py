from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='rental-home'),
    path('about/', views.about, name='rental-about'),
]
