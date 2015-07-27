from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^$',scan, name='scan'),
	url(r'^views/$',views, name='views'),
)