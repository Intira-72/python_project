from django.contrib import admin
from django.urls import path, re_path

from . import views
from accounts.views import login_view
from asticles.views import (
    article_view,
    article_search_view,
    article_create_form
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', login_view),
    path('articles/', article_search_view),
    path('articles/create/', article_create_form),
    path('articles/<int:pk>/', article_view),    
]
