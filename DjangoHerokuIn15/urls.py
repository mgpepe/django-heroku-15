from django.conf.urls import patterns, include, url
from DjMainApp import views as main_views
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', main_views.splash, name="splash"),
    url(r'^login$', main_views.login_view, name="login"),
    url(r'^signup$', main_views.register, name="signup"),
    url(r'^forgot$', main_views.forgot_pass, name="forgotmypass"),
    url(r'^set_new_pass/([-\w]+)/$', main_views.set_new_pass, name="set_new_pass"),
    url(r'^logout$', main_views.logout_user, name="logout"),
    url(r'^dashboard$', main_views.home, name="home"),
    # Examples:
    # url(r'^$', 'DjangoHerokuIn15.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
