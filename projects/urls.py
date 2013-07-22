from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView


urlpatterns = patterns('projects',
	url(r'^$', TemplateView.as_view(template_name='projects/project_list.html'), name='project_list'),
	url(r'^(?P<project_id>(\d+))/$', TemplateView.as_view(template_name='projects/project_detail.html'), name='project_detail'),
)
