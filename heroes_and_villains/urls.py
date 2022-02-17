from . import views
from django.urls import path

urlpatterns = [
    path('', views.heroes_and_villains_list),
    path('<int:pk>/', views.heroes_and_villains_detail),
]