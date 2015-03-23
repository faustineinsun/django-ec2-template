from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import polls.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', polls.views.index, name='index'),
    url(r'^db', polls.views.db, name='db'),
    #url(r'^polls/', include('polls.urls')), # Namespacing URL names https://docs.djangoproject.com/en/1.7/intro/tutorial03/
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    )
