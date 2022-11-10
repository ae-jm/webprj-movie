from django.urls import path, include
from recommand import views

urlpatterns = [
    path('', views.home),
    path('list/', views.movielist),
    path('search/', views.search, name='search'),
]
