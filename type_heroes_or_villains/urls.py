from . import views
from django.urls import path

urlpatterns = [
    path('', views.type_heroes_or_villains_list),
]