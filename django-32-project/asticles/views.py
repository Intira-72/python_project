from django.shortcuts import render
from .models import Article

# Article All View
def article_view(request, pk=None):
    if pk is not None:
        article_obj = Article.objects.get(pk=pk)
        context = {'article_obj': article_obj}
    else:
        context = {'article_obj': None}

    return render(request, "article_detail_view.html", context=context)


# Article Search View
def article_search_view(request):
    
    try:
        query = int(request.GET['q'])
    except:
        query = None


    if query is not None:
        article_queryset = [Article.objects.get(pk=query)]
    else:
        article_queryset = Article.objects.all()

    context = {
        'article_queryset': article_queryset
    }

    return render(request, "article_search_view.html", context=context)