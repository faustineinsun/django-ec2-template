from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
                       # ex: /polls/
                       # ex: /polls/5/
                       # ex: /polls/5/results/
                       # ex: /polls/5/vote/

                       #url(r'^$', views.indexpolls, name='indexpolls'),
                       #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
                       #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

                       url(r'^$', views.IndexpollsView.as_view(), name='indexpolls'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
                      )
