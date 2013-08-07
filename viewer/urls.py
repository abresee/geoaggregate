from django.conf.urls.defaults import *

urlpatterns = patterns('viewer.views',
    url(r'^$', 'index', name='viewer-index'),
    url(r'^query$', 'query', name='viewer-query'),
)
    
