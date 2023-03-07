from django.shortcuts import render
from .models import Article

# Create your views here.
def article_view(request, pk=None):
    if pk is not None:
        article_obj = Article.objects.get(pk=pk)
        context = {'article_obj': article_obj}
    else:
        context = {'article_obj': None}

    return render(request, "article_detail_view.html", context=context)