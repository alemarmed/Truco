from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from rest_framework.generics import SingleObjectAPIView
from ws_views import RegisterView
from models import Users
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server_truco.views.home', name='home'),
    # url(r'^server_truco/', include('server_truco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$',RegisterView.as_view(),name="register"),
)
