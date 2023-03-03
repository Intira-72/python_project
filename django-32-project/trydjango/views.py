from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

from asticles.models import Article


def home(request):
    article_obj = Article.objects.all().order_by("?").first()

    context = {
        'id': article_obj.id,
        'title': article_obj.title,
        'content': article_obj.content
    }

    tmpl = get_template("home_view.html")
    html_str = tmpl.render(context=context)

    # the same
    # html_str = render_to_string("home_view.html", context=context)
    
    return HttpResponse(html_str)