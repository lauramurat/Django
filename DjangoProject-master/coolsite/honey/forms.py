from django import forms
from .models import *



class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    brand = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    price = forms.CharField(max_length=255)
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all())

