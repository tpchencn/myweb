from django.db import models
from mdeditor.fields import MDTextField


class Topic(models.Model):
    """ 用户学习的主题 """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.text


class Entry(models.Model):
    """ 学到的有关某个主题的具体知识 """
    topic = models.ForeignKey(Topic, on_delete=True)
    title = models.CharField(max_length=20, blank=True)
    # text = models.TextField(blank=True)
    content = MDTextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.title[:50]


class Books(models.Model):
    """ 用户学习的主题 """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.text


class ReadNote(models.Model):
    """ 学到的有关某个主题的具体知识 """
    topic = models.ForeignKey(Books, on_delete=True)
    title = models.CharField(max_length=20, blank=True)
    # text = models.TextField(blank=True)
    content = MDTextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.title[:50]
