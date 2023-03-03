from django.http import HttpResponse
import random


def home(request):
    number = random.randint(10, 123456)

    u_name = "Justin"
    html_str = f"""<h1>Hello, {u_name} - {number}.</h1>"""
    
    return HttpResponse(html_str)