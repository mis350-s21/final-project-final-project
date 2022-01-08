from django.urls import path
from .import views
urlpatterns = [
    path('', views.greeting, name='home'),
    path('search', views.search, name='search'),
]