from django.conf.urls import url, include
from . import views

app_name='newshome'
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^result/$', views.result, name='result'),
url(r'^vote/$', views.vote, name='vote'),
url(r'^aboutus/$', views.aboutus, name='aboutus')
]