from django.urls import path

from .views import *


app_name = 'news'

urlpatterns = [
    path('', views.get_articles, name='get-articles')
]