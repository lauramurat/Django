from django import forms
from jsonschema.exceptions import ValidationError

from .models import *



class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"


    class Meta:
        model = Product
        fields = ['name', 'slug', 'brand', 'content', 'photo', 'price', 'is_published', 'cat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'brand': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

        def clean_name(self):
            name = self.cleaned_data['title']
            if len(name) > 200:
                raise ValidationError('Dlina prevyshaet 200 simvolov')
            return name

    # name = forms.CharField(max_length=255, label="Аты", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # brand = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label="Бренд")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label="Контент")
    # price = forms.CharField(max_length=255, label="Багасы")
    # is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категориялар",  empty_label="Категория тандалмады")

