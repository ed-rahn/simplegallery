from django.conf.urls.defaults import patterns, url

from views import AuthorListView, AuthorDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', AuthorListView.as_view(), name='authors'),
    url(r'^(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='authors-detail'),
)
