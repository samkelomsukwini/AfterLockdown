from django.urls import path

from .views import view_post


app_name = 'afterlockdown'

urlpatterns = [
    path('<call_id>/', view_post, name='view-post'),
]