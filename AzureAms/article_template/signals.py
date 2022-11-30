from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Article
 
 
# @receiver(post_save, sender=Article)
# def reorder(sender, instance, **kwargs):
#     article_change = instance
#     order_change = instance.order
#     articles = Article.objects.all()
    