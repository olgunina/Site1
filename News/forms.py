import re

from django import forms
from .models import Category, News
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title
    
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }
#    title = forms.CharField(max_length=150, label='Заголовок')