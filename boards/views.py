# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from boards.models import Board, Topic, Post, Article, Category, Comment as JKComment
from boards.forms import NewTopicForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    boards = Board.objects.all()
    hotnews = Article.objects.filter(is_hotnews=True).latest('created_at')
    topviewed = Article.objects.filter(is_topviewed=True).exclude(slug=hotnews.slug)[0:2]
    ctx ={
        'cateogries': categories,
        'boards':boards,
        'hotnews':hotnews,
        'topviewed' :topviewed,
    }
    return render(request, 'technews/index.html', ctx)


def category(request, name):
    categories = Category.objects.all()
    boards = Board.objects.all()
    hotnews = Article.objects.filter(is_hotnews=True).latest('created_at')
    topviewed = Article.objects.filter(is_topviewed=True).exclude(slug=hotnews.slug)[0:2]
    ctx ={
        'cateogries': categories,
        'boards':boards,
        'hotnews':hotnews,
        'topviewed' :topviewed,
    }
    return render(request, 'technews/index.html', ctx)


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=1, pk=1)
    return render(request, 'topic_posts.html', {'topic': topic})

##################### TECHNEWS ####################




