from django.db import models


  
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=4000)
    
