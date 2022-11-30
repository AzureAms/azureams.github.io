from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Article, Core


def view_article(request):
    myarticles = Article.objects.all().values()
    #update order
    prev = 0
    for article in Article.objects.all():
        if article.order != prev+1:
            temp = article.order
            article.order = prev+1
            Article.objects.get(order=temp).delete()
        prev += 1
        article.save()
    #update order complete
    template = loader.get_template('view_article.html')
    context = {
    'myarticles': myarticles,
    }
    return HttpResponse(template.render(context, request))
  
def index(request):
    myarticles = Article.objects.all().values()
    #update order
    prev = 0
    for article in Article.objects.all():
        if article.order != prev+1:
            temp = article.order
            article.order = prev+1
            Article.objects.get(order=temp).delete()
        prev += 1
        article.save()
    #update order complete
    cores = Core.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'myarticles': myarticles[len(myarticles)-3:],
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['title']
    y = request.POST['content']
    article = Article(title=x, content=y)
    article.tomtat = request.POST['tomtat']
    article.type = request.POST['type']
    article.save()
    article.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, order):
    article = Article.objects.get(order=order)
    article.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, order):
    myarticle = Article.objects.get(order=order)
    template = loader.get_template('update.html')
    context = {
    'myarticle': myarticle,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, order):
    article = Article.objects.get(order=order)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.order = request.POST['order']
    article.tomtat = request.POST['tomtat']
    article.type = request.POST['type']
    article.save()
    return HttpResponseRedirect(reverse('index'))

