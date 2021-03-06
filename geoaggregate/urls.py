from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tiger.views.index'),
    url(r'^demo/(?P<state>\w+)/(?P<county>\w+)', 'tiger.views.demo')
)
