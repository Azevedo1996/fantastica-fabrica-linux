from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.home, name='home'),
    path('iniciar/', views.start_game, name='start'),
    path('missao/', views.mission, name='mission'),
    path('reiniciar/', views.restart, name='restart'),
]
