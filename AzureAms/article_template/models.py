from django.db import models


  
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tomtat = models.CharField(max_length=500)
    type = models.CharField(max_length=225)
    order = models.PositiveIntegerField()
    image1 = models.TextField()
    image2 = models.TextField()
    
    class Meta:
        ordering = ('order',)
    
    def __str__(self):
        return self.title


positionToChoose = (('President', "President"), 
                    ('Vice President', "Vice President"), 
                    ('Project Leader', "Project Leader"), 
                    ('Head of Pr', "Head of Pr"), 
                    ('Head of Events', "Head of Events"), 
                    ('Head of Medes', "Head of Medes"),
                    )
class Core(models.Model):
    name = models.CharField(max_length=1000)
    image = models.TextField()
    url = models.TextField()
    url_type = models.CharField(max_length=100, choices=(("fab fa-facebook text-gray-300 text-lg md:text-xl", "facebook"),("fab fa-github mr-1", "github")))
    url_name = models.CharField(max_length=15)
    position = models.CharField(max_length=100, choices=positionToChoose)
    order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ('order',)