from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^$', 'waybill.views.scan', name='scan'),
	url(r'^waybill/',include('waybill.urls')),
	# url(r'^city/',include('city.urls')),
	# url(r'^insert/',include('insert.urls')),
	# url(r'^search/',include('search.urls')),

)
