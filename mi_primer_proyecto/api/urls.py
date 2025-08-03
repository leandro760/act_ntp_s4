from django.urls import path
from .views import HelloWorldView, greet_view

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('greet/', greet_view, name='greet'),
]
