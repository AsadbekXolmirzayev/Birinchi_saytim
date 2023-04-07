from django.contrib import admin
from .models import Article, Tag, Category, Comment, ExtraText, ExtraImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_filter = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'article', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['article__title', 'author__username', 'author__firs_name', 'author__last_name']
    autocomplete_fields = ['author', 'article']


@admin.register(ExtraImage)
class ExtraPic(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ExtraText)
class Extratext(admin.ModelAdmin):
    list_display = ['id', 'description']
