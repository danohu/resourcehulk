from django.conf.urls import patterns, url

from hulk import views

urlpatterns = patterns('',
    url(r'company/(?P<company_id>\d+)/?$', views.company, name='company'),
    url(r'project/(?P<project_id>\d+)/?$', views.project, name='project'),
    url(r'^$', views.index, name='index'),

)
