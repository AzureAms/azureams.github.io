from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Article


def index(request):
    myarticles = Article.objects.all().values()
    #update ID
    prev = 0
    for article in Article.objects.all():
        if article.id != prev+1:
            temp = article.id
            article.id = prev+1
            Article.objects.get(id=temp).delete()
        prev += 1
        article.save()
    #update ID complete
    template = loader.get_template('index.html')
    context = {
    'myarticles': myarticles,
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

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myarticle = Article.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'myarticle': myarticle,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.id = request.POST['id']
    article.tomtat = request.POST['tomtat']
    article.type = request.POST['type']
    article.save()
    return HttpResponseRedirect(reverse('index'))

