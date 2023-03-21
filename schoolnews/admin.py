from django.contrib import admin
from schoolnews.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

admin.site.register(Article, ArticleAdmin)
