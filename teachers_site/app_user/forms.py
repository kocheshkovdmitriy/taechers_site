from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthUser(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    slug = forms.CharField(max_length=20, required=False, help_text='URL, только латинские буквы')
    city = forms.CharField(required=False, help_text='Город')
    school = forms.CharField(required=False, help_text='Школа')
    grade = forms.IntegerField(required=False, help_text='Только число, без букв')




    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)