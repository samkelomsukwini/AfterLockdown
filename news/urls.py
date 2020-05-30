from django.urls import path

from . import views


app_name = 'news'

urlpatterns = [
    path('', views.get_articles, name='get-articles'),
    path('<call_id>/', views.go_to_url, name='go-to-url')
]