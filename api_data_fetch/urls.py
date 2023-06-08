from django.urls import path
from . import views

urlpatterns = [
    path('', views.instagram_feed, name='insagram_feed')
]
