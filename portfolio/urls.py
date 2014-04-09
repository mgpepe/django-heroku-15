from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^$', 'portfolio.views.home', 
			name = 'psplash'),
		url(r'^(?P<portfolio_id>\d+)/$', 'portfolio.views.single', name = 'single'),
)
