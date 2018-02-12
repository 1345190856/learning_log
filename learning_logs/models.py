# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)  # 自动设置为当前时间
    owner = models.ForeignKey(User)

    def __str__(self):  # py27用__unicode__()
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'  # 需要时用entries表示多个条目

    def __str__(self):
        if len(self.text) > 50:
            return self.text[0:50] + '...'
        else:
            return self.text








