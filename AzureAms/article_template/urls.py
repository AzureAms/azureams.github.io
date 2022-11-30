from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_article, name='index'),
    path('article/<int:order>', views.article_page, name="article_page"),

]