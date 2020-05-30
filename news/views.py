from django.shortcuts import render

from .models import News


def get_articles(request):
    articles = News.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'news/articles.html')