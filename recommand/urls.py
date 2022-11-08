from django.urls import path, include
from recommand import views
from .views import search

urlpatterns = [
    path('', views.home),
    path('ost_search/', views.ost_search),
]
