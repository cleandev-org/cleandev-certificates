from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cleandevcertificates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^core/', include('cleandevcertificates.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
