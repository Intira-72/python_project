from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

from asticles.models import Article
import random


def home(request, *args, **kwargs):
    article_obj = Article.objects.get(pk=random.randint(1, 3))
    article_queryset = Article.objects.all()

    context = {'article_queryset': article_queryset,
               'article_obj': article_obj}

    tmpl = get_template("home_view.html")
    html_str = tmpl.render(context=context)

    # the same
    # html_str = render_to_string("home_view.html", context=context)
    
    return HttpResponse(html_str)