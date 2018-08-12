from django.urls import path
from . import views

urlpatterns = [
    path('createclub/', views.create_club, name='create_club'),
    path('movieclub/<slug:slug>/', views.club_page, name='club_page')
]
