from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^aboutus/$', views.aboutus, name='aboutus'),
	url(r'^posts/$', views.posts, name='posts'),
	url(r'^event/$', views.event, name='event'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^contributors/$', views.contri, name='contri')
]