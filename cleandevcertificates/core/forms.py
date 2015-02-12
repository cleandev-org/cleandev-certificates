# coding: utf-8
from django import forms
from localflavor.br.forms import BRCPFField
from django.core.exceptions import ValidationError
from .models import _, Person


def email_is_unique(value):
    if Person.objects.filter(email__exact=value).count():
        raise ValidationError(_(u'Email já cadastrado no sistema.'))


class PersonForm(forms.ModelForm):
    cpf = BRCPFField(label=_(u'CPF'))

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['university'].required = True
        self.fields['course'].required = True
        self.fields['email'].required = True
        self.fields['email'].validators.append(email_is_unique)

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
