from .models import Blog
from django.forms import ModelForm
from django.forms import TextInput, Textarea


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']

        widgets = {
                    'title': TextInput(attrs={
                        'class': 'form-item text-input',
                        'placeholder': 'Название'
                    }),
                    'text': Textarea(attrs={
                        'class': 'form-item text-input',
                        'placeholder': 'Текст',
                        'cols': '30',
                        'rows': '10'
                    }),
                }
