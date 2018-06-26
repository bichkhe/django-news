# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from boards.models import Board, Topic, Post, Article, Category, SubCategory, Comment as JKComment, SubComment
# Register your models here.


admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(JKComment)
admin.site.register(SubComment)
