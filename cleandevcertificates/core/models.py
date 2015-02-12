# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import KindPersonManager


class Person(models.Model):
    KIND_CHOICES = (
        ('S', _(u'Aluno')),
        ('U', _(u'Universidade')),
        ('P', _(u'Patrocinador')),
    )

    kind = models.CharField(_(u'tipo'), max_length=1,
                            choices=KIND_CHOICES, default="S")
    university = models.ForeignKey('self', verbose_name=_(
        u'faculdade'), blank=True, null=True,
        limit_choices_to={'kind__in': ['U']})
    course = models.CharField(_(u'curso'), max_length=100, blank=True)
    semester = models.IntegerField(_(u'semestre'), blank=True, null=True)
    name = models.CharField(_(u'nome'), max_length=100)
    display_name = models.CharField(_(u'apelido'), max_length=100, blank=True)
    cpf = models.CharField(_(u'CPF'), max_length=20, blank=True)
    email = models.EmailField(_(u'e-mail'), max_length=100, blank=True)
    city = models.CharField(_(u'cidade'), max_length=50, blank=True)
    facebook = models.URLField(_(u'facebook'), blank=True)
    twitter = models.CharField(_(u'twitter'), max_length=50, blank=True)
    image = models.CharField(_(u'URL imagem'), max_length=250, blank=True)
    order = models.PositiveIntegerField(_(u'ordem de exibição'), default=0)
    is_active = models.BooleanField(_(u'ativo?'), default=True)
    created_at = models.DateTimeField(_(u'criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'alterador em'), auto_now=True)

    objects = models.Manager()
    students = KindPersonManager('S')
    universities = KindPersonManager('U')
    places = KindPersonManager(['U', 'P'])

    class Meta:
        verbose_name = _(u'Pessoa')
        verbose_name_plural = _(u'Pessoas')
        ordering = ['order', 'name']

    def __unicode__(self):
        if self.kind in ['U', 'P']:
            return '%s - %s' % (self.name, self.city)
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:person_edit', (), {})

    def verify(self):
        try:
            self = Person.objects.get(cpf=self.cpf, email=self.email)
            return self
        except:
            return None

    def courses(self):
        return self.person_set.all().order_by('course').distinct('course')

    def events(self):
        return self.certfied.events_set.filter(is_active=True)

    def certficates(self):
        return self.certfied_set.filter(is_active=True)
