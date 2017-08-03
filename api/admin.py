from django.contrib import admin
from .models import Author
from .models import Article
from .models import Board
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ('author', 'label', 'title', 'dateTime', "text")
    list_display = ('author', 'label', 'title', 'dateTime')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ("authorName", )
    list_display = ("authorName", )

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    fields = ("BoardName", )
    list_display = ("BoardName", )