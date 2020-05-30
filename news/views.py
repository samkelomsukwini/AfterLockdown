from django.core.paginator import Paginator

from django.shortcuts import Http404, redirect, render

from .models import News


def get_articles(request):
    articles = News.objects.all()
    paginator = Paginator(articles, 5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'articles': articles
    }

    return render(request, 'news/articles.html', context)



def go_to_url(request, call_id):
    try:
        article = News.objects.get(call_id=call_id)
        return redirect(f'{article.url}')
    
    except:
        raise Http404()