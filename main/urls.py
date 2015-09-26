from django.conf.urls import patterns, include, url

import session_csrf

session_csrf.monkeypatch()

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'main.views.index', name='index'),
                       url(r'^_ah/', include('djangae.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^csp/', include('cspreports.urls')),
                       url(r'^auth/', include('djangae.contrib.gauth.urls')),
                       )
