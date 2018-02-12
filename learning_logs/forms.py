# -*- coding: utf-8 -*-

from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # 根据Topic创建表单
        fields = ['text']  # 只包含字段text
        labels = {'text': ''}  # 不为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # widgets小部件，覆盖默认部件

