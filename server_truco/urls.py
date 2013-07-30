from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Views:
    url(r'^client/',include('truco.core.client.urls')),
    url(r'^$', 'core.views.home', name='home'),
    
    #core
    url(r'^store/new/$',"core.store.views.create_store", name="create_store"),
    url(r'^ajax/get_cities/$', 'core.views.get_cities', name='get_cities'),    
    url(r'^login/$', 'core.views.login_view', name='login'),
    url(r'^my-stores/$', "core.views.list_stores", name="list_stores"),
    url(r'^store/edit/(?P<id_store>\w+)/', "core.views.store_form", name="store_form"),
    #url(r'^store/new/$', "core.views.store_form", name="new_store"),
    url(r'^store/places_form/$', "core.views.load_place_form", name="load_place_form"),    
    url(r'^login/$', 'core.views.login_view', name='login'),
    url(r'^store/delete/$','core.views.delete_store',name='delete_store'),
    url(r'^store/(?P<id_store>\w+)/products','core.views.products',name='store_products'),
    url(r'^store/(?P<id_store>\w+)/place/(?P<id_place>\w+)/products','core.views.products',name='place_products'),
    # AJAX
    url(r'^subcategories/$','core.views.get_subcategories',name='subcategories'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.customManager.urls')),
    url(r'^admintools/', include('admin_tools.urls')),    
    #url(r'^api/csrf','core.api_mobile.get_csrf'),
)

# Serving statics in DEVELOPMENT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))
