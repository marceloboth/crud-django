# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^clientes/', include('clientes.urls', namespace='clientes')),    
    
    url(r'^admin/', include(admin.site.urls)),
)

# arquivos estáticos
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns