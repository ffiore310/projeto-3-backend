from django.urls import path

from . import views

urlpatterns = [
    path('api/users/', views.api_user),
    path('api/token/', views.api_get_token),
    path('api/favoritos/', views.api_favoritos),
    path('api/soccer/', views.api_soccer),
    path('api/soccer/table', views.api_soccer_table),
    path('api/soccer/games', views.api_soccer_games),
    path('api/favorita', views.api_favorita_time),
]