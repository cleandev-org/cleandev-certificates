# coding: utf-8
from django import forms
from localflavor.br.forms import BRCPFField
from django.core.exceptions import ValidationError
from .models import _, Person


class PersonForm(forms.ModelForm):
    cpf = BRCPFField(label=_(u'CPF'))

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['university'].required = True
        self.fields['course'].required = True
        self.fields['email'].required = True

    class Meta:
        model = Person
        fields = ('name', 'cpf', 'email', 'email', 'city', 'university',
                  'course', 'semester', 'facebook', 'twitter')
        widgets = {
            'kind': forms.HiddenInput()
        }


class FormLogin(forms.Form):
    cpf = forms.CharField(label=_('CPF'))
    email = forms.EmailField(label=_('E-mail'))
