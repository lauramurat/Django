from django import forms
from .models import *



class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255, label="Аты", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    brand = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label="Бренд")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label="Контент")
    price = forms.CharField(max_length=255, label="Багасы")
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категориялар",  empty_label="Категория тандалмады")

