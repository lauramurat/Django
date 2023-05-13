from aiogram.types import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from jsonschema.exceptions import ValidationError
from captcha.fields import CaptchaField
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

class RegisterUserForm(UserCreationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        captcha = CaptchaField()

        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2','captcha')

class LoginUserForm(AuthenticationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class BailanysForm(forms.Form):

    class Meta:
        model = Bailanys
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'cols': 60, 'rows': 10}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

        def clean_name(self):
            name = self.cleaned_data['name']
            if len(name) > 200:
                raise ValidationError('Dlina prevyshaet 200 simvolov')
            return name



class NewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }
