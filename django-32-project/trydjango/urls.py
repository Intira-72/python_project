from django.contrib import admin
from django.urls import path, include

from . import views
from asticles.views import article_view, article_search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('articles/', article_search_view),
    path('article/<int:pk>/', article_view),    
]
