from django import forms
from . import models

choices = [
    ('Private','Private'),
    ('Public','Public'),
]

class CreateArticle(forms.ModelForm):
    type = forms.ChoiceField(label='Type',choices=choices,widget=forms.RadioSelect())
    title = forms.CharField(label='Title', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Title','autocomplete':'off'}))
    slug = forms.CharField(label='Slug', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Slug','autocomplete':'off'}))

    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb','type']

