# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse as r
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import base, TemplateView, ListView
from cleandevcertificates.core.views import logged
from .models import Event, Certified


class CertifiedListView(ListView):
    model = Certified
    template_name = "certified_list.html"
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedListView, self)\
            .dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects\
            .filter(person=self.request.session['person']['pk'])


class CertifiedView(base.View):
    template_name = 'certified_form.html'
    model_event = Event
    certified = None
    event = None

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        self.event = self.get_event(request)
        self.certified = self.get_object(request)

        if request.is_ajax():
            return HttpResponse(self.get_success_url(), status=300)

        return HttpResponseRedirect(self.get_success_url())

    def get_event(self, request):
        return get_object_or_404(self.model_event,
                                 token__exact=request.POST.get('token'))
                                 # token_expirate__lte=date.today())

    def get_object(self, request):
        certified, created = Certified.objects.get_or_create(
            event=self.event, person_id=request.session['person']['pk'])
        return certified

    def get_success_url(self):
        return r("events:certified_detail", args=[],
                 kwargs={'pk': self.certified.pk})


class CertifiedDetailView(base.View):
    model = Certified
    template_name = "certified_detail.html"
    certified = None

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedDetailView, self).dispatch(request,
                                                         *args, **kwargs)

    def get(self, request, *args, **kwargs):
        certified = self.get_object(request, kwargs.get('pk'))

        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        self.get_object(request, kwargs.get('pk'))
        action = request.POST.get("_action")

        if action == "rating":
            return self.rating(request)

        if action == "send":
            pass
            # return self.send_certified(request)

        return HttpResponseRedirect(r("events:certified_detail", args=[],
                                      kwargs={'pk': self.certified.pk}))

    def get_object(self, request, pk):
        self.certified = get_object_or_404(
            self.model, pk=pk, person=request.session['person']['pk'])
        return self.certified

    def rating(self, request):
        certified = self.certified
        certified.rating = request.POST.get("rating")
        certified.observation = request.POST.get("observation")
        certified.save()

        if request.is_ajax():
            return HttpResponse(u'Classificação efetuada com sucesso',
                                status=200)

        return render(request, self.template_name, locals())

    def send_certified(self, request):
        body = render_to_string(
            'emails/certified_mail.html', {'object': self.certified})
        subject = 'Certificado CleaDev.org'

        send_mail(subject, '', 'matheus@coder42.com',
                  [self.certified.person.email], html_message=body)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return r("events:certified_success")


class CertifiedPrintView(base.View):
    model = Certified
    template_name = 'certified_template.html'

    def dispatch(self, request, *args, **kwargs):
        if not logged(request):
            return HttpResponseRedirect(r('core:login'))

        return super(CertifiedPrintView, self).dispatch(request,
                                                        *args, **kwargs)

    def get(self, request, pk):
        return render(request, self.template_name, {
            'object': self.get_object()})

    def get_object(self):
        return self.model.objects.get(
            pk=self.kwargs.get('pk'),
            person=self.request.session['person']['pk'])

    def report(self):
        pass
        # Reportlab
        # lwidth, lheight = letter
        # p = canvas.Canvas(response, pagesize=(lheight, lwidth))
        # p.drawString(0, 600, self.get_template())
        # p.showPage()
        # p.save()

        # response = HttpResponse(f, content_type='application/pdf')
        # response['Content-Disposition'] = 'filename="{name}.pdf"'.format(
        #     name=self.object.event.name)

        # return response


class CertifiedSuccessView(TemplateView):
    template_name = "certified_success.html"
