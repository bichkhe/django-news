# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    
 class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='categories')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    is_priority = models.BooleanField()

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='categories')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    category = models.ForeignKey(Category, related_name='subcategories')
    
    
class Comment(models.Model):
    abstract = models.CharFiled(max_length=500)
    message = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_hidden =  models.BooleanField()
    articles = models.ForeignKey(Article, null=True, related_name='comments')

class SubComment(models.Model):
    is_subcomment = models.BooleanField()
    abstract = models.CharFiled(max_length=500)
    message = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    is_hidden =  models.BooleanField()
    subcomments = models.ForeignKey(Comment, null=True, related_name='subcomments')
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharFiled(max_length=500)
    image = models.ImageField(upload_to = 'static/uploads/', default = '')
    image_small = models.ImageField(upload_to = 'static/uploads/', default = '')
    message = models.TextField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='categories')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    category = models.ForeignKey(Category, related_name='subcategories')
    is_hotnews= models.BooleanField()
    is_topviewed = models.BooleanField()
    iranks = models.IntegerField()
    iviews = models.IntegerField()
    ishared = models.IntegerField()
   




    
