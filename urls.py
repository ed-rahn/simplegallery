from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import WelcomeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', WelcomeView.as_view(), name='home'),
    url(r'^authors/', include('simplegallery.authors.urls')),
    url(r'^gallery/', include('simplegallery.gallery.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
