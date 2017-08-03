from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    authorID = models.AutoField(primary_key=True)
    authorName = models.CharField(max_length=255)
    def __str__(self):
        return self.authorName

class Board(models.Model):
    boardID = models.AutoField(primary_key=True)
    BoardName = models.CharField(max_length=255)
    def __str__(self):
        return self.BoardName
# Create your models here.
class Article(models.Model):
    postID = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author)
    label = models.ForeignKey(Board)
    dateTime = models.CharField(max_length=30)
    title = models.CharField(max_length=400)
    text = models.TextField()