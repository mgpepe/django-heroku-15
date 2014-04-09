from django.conf.urls import patterns, include, url
from django.conf import settings
from portfolio import views
# from django.views.generic.simple import direct_to_template
# from django.views.generic import TemplateView



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', "DjMainApp.views.splash", name="splash"),
    url(r'^login$', "DjMainApp.views.login_view", name="login"),
    url(r'^signup$', "DjMainApp.views.register", name="signup"),
    url(r'^forgot$', "DjMainApp.views.forgot_pass", name="forgotmypass"),
    url(r'^set_new_pass/([-\w]+)/$', "DjMainApp.views.set_new_pass", name="set_new_pass"),
    url(r'^logout$', "DjMainApp.views.logout_user", name="logout"),
    url(r'^dashboard$', "DjMainApp.views.home", name="home"),
    (r'^portfolio/', include('portfolio.urls')),
    # Examples:
    # url(r'^$', 'DjangoHerokuIn15.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
