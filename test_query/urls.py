from django.conf.urls.defaults import *

urlpatterns = patterns('test_query.views',
    url(r'^$', 'index', name='test_query-index'),
    url(r'^query$', 'query', name='test_query-query'),
)
    
