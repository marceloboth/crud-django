from django.conf.urls.defaults import *

urlpatterns = patterns('clientes.views',
    url(r'^$', 'list', name='list'),
    url(r'^create/$', 'create', name='create'),
    url(r'^delete/(?P<id>\d+)$', 'delete', name='delete'),
    url(r'^update/(?P<id>\d+)$', 'update', name='update'),
)