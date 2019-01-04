from .models import Catego, Post
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class DupaForm(forms.Form):
    class Meta:
        model = Catego
        fields = ['name']
        labels = {'name': ''}


class PepekForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'slug', 'title']
        labels = {'text': '', 'slug': 'slugers', 'title': 'Title'}
        widgets = {'text': forms.Textarea(attrs={'cols': 90})}
