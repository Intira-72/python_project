from django.http import HttpResponse
import random

from asticles.models import Article


def home(request):
    my_post = Article.objects.all().order_by("?").first()
    
    html_str = f"""<h1>Title: {my_post.title}</h1>
                    <p>content: {my_post.content}</p>"""
    
    return HttpResponse(html_str)