"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article_template import views

urlpatterns = [
    path('', views.view_article, name='index'),
    path('AzureAms/', include('article_template.urls')),
    path('addArticle', views.view_article, name='index'),
    path('admin/', admin.site.urls),
    path('add/',views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:order>', views.delete, name='delete'),
    path('update/<int:order>', views.update, name='update'),
    path('update/updaterecord/<int:order>', views.updaterecord, name='updaterecord'),
    path('index.html', views.index, name='index.html')

]
