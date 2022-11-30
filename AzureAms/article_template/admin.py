from django.contrib import admin

from .models import Article, Core


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['order', 'title']

@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    list_display = ['order', 'position', 'name']