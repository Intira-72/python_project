from django.contrib import admin
from django.urls import path

from . import views
from asticles.views import article_view, article_search_view, article_create_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('articles/', article_search_view),
    path('articles/create/', article_create_form),
    path('article/<int:pk>/', article_view),    
]
