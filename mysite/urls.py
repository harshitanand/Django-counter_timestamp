from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *
from counter.views import *


urlpatterns = patterns('',
    # Examples:
    url (r'^$', main_page),
    # url(r'^blog/', include('blog.urls')),
    url (r'^hello/$', hello ),
    url (r'^time/$', time), 
    url (r'^time/plus/(\d{1,2})/$', times_ahead),
    url (r'^admin/', include(admin.site.urls)),
)
