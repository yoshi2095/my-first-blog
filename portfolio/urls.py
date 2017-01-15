from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.project_list, name='project_list'),
	url(r'^project/(?P<pk>\d+)$', views.project_detail, name='project_detail'),
	url(r'^project/new/$', views.project_new, name='project_new'),
	url(r'^project/(?P<pk>\d+)/edit/$', views.project_edit, name='project_edit'),
	url(r'^drafts/$', views.project_draft_list, name='project_draft_list'),
	url(r'^project/(?P<pk>\d+)/publish/$', views.project_publish, name='project_publish'),
	url(r'^project/(?P<pk>\d+)/remove/$', views.project_remove, name='project_remove'),
	url(r'^project/(?P<pk>\d+)/comment/$', views.add_comment_to_project, name='add_comment_to_project'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	url(r'^aboutme/$', views.about_me, name='about_me'),
	#url(r'^thanks/$', views.thanks,name='thanks'),
]