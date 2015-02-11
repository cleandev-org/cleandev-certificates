# coding: utf-8
from django import forms
from .models import _, Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['kind'].widget = forms.HiddenInput()
        self.fields['email'].required = True


class FormLogin(forms.Form):
    cpf = forms.CharField(label=_('CPF'))
    email = forms.EmailField(label=_('E-mail'))
