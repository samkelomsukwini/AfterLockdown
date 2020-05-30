from django.shortcuts import render

from afterlockdown.views import get_posts

def index(request):
    posts = get_posts(request)
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)