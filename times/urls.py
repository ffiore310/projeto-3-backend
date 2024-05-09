from django.urls import path

from . import views

urlpatterns = [
    path('api/users/', views.api_user),
    path('api/token/', views.api_get_token),
    path('api/favoritos/', views.api_favoritos),
]