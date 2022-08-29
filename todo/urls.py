from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name='home'),
    path('add/', todo_create, name='add')
]