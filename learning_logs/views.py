from django.shortcuts import render
from .models import Topic


def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ 显示所有的主题 """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ 显示单个主题及其所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all().order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def about(request):
    """ 显示网站信息"""
    return render(request, 'learning_logs/about.html')


def books(request):
    """ 显示所有的主题 """
    bookname = books.objects.order_by('date_added')
    context = {'topics': bookname}
    return render(request, 'learning_logs/topics.html', context)


def readnote(request, books_id):
    """ 显示单个主题及其所有的条目 """
    book = Topic.objects.get(id=books_id)
    entries = book.entry_set.all().order_by('-date_added')
    context = {'book': book, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
