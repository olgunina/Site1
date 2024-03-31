import re

from django import forms
from django.forms import SelectDateWidget

from .models import Profession, Human
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class HumanForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['name_surname']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = Human
        fields = ['name_surname', 'biografia', 'birthdate', 'profession']
        widgets = {
            'name_surname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10
            }),
            'birthdate': SelectDateWidget(years=range(1940, 2014)),
            'profession': forms.Select(attrs={
                'class': 'form-control'
            })
        }
