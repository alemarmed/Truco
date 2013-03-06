from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'server_truco.views.home', name='home'),
    url(r'^my-stores$', "server_truco.views.list_stores", name="list_stores"),
    url(r'^store/(?P<id>\w+)/', "server_truco.views.store_form", name="store_form"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
