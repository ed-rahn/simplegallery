from django.conf.urls.defaults import patterns, url

from views import GalleryView, GalleryDetailView, GalleryByAuthorView, GalleryByTitleView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery-detail'),
    url(r'^byauthor/(?P<authorname>\w+)/$', GalleryByAuthorView.as_view(), name='gallery-byauthor'),
    url(r'^search-by-title$', GalleryByTitleView.as_view(), name='search-by-title'),
)
