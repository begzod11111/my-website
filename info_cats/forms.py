from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *


class ArticleForm(ModelForm):
    class Meta:
        model = ArticleCat
        fields = ['title', 'font', 'text', 'author']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-input style-all-button',
                'placeholder': 'Заголовок'
                                      }),
            'text': Textarea(attrs={'class': 'style-all-button text-input'}),
            'font': FileInput(attrs={'class': 'file-input form-label'})

        }
        labels = {
            'title': "",
            'font': '',
            'text': '',
        }

