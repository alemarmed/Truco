from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^my-stores/$', "app.views.list_stores", name="list_stores"),
    url(r'^store/edit/(?P<id_store>\w+)/', "app.views.store_form", name="store_form"),
    url(r'^store/new/$', "app.views.store_form", name="new_store"),
    url(r'^login/$', 'app.views.login_view', name='login'),
    url(r'^store/save_location','app.views.save_location',name='save_location'),
    url(r'^store/delete/$','app.views.delete_store',name='delete_store'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.customManager.urls')),
    url(r'^admintools/', include('admin_tools.urls')),
)

# Serving statics in DEVELOPMENT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))
