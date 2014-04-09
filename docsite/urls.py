from django.conf.urls import patterns, include, url
from docsite.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
