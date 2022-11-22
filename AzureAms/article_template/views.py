from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Article


def index(request):
    myarticles = Article.objects.all().values()
    #update ID
    prev = 0
    for member in Article.objects.all():
        if member.id != prev+1:
            temp = member.id
            member.id = prev+1
            Article.objects.get(id=temp).delete()
        prev += 1
        member.save()
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
    member = Article(title=x, content=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Article.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myarticle = Article.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'myarticle': myarticle,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    title = request.POST['title']
    content = request.POST['content']
    idToChange = request.POST['id']
    member = Article.objects.get(id=id)
    member.title = title
    member.content = content
    member.id = idToChange
    member.save()
    return HttpResponseRedirect(reverse('index'))