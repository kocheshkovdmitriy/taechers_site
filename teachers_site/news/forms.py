from django import forms
from .models import New, Commit


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'


class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(), 'user_name': forms.HiddenInput(), 'new': forms.HiddenInput()}