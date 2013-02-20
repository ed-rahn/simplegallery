from django.db import models
from authors.models import Author

from tasks import download_image

class Image(models.Model):
    """Gallery image, linked to an Author"""
    author = models.ForeignKey(Author, related_name='images')
    timestamp = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=250)
    hash = models.CharField(max_length=10)
    ext = models.CharField(max_length=4)
    size = models.PositiveIntegerField()
    url = models.URLField(verify_exists=False, max_length=200, blank=True)
    thumbnail_url = models.URLField(verify_exists=False, max_length=200, blank=True)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('gallery-detail', [self.pk])

    def build_urls(self):
        """
        Using the `hash` and `ext` members of the image, builds the URL of
        the image on the Imgur server. Also, by using the `hash`, the extension
        '.jpg' and a special pattern, we can generate the URL for the image's
        thumbnail.
        """
        # TODO: complete this by browsing around Imgur for a bit and checking
        # what the URL patterns looks like
        self.url = "http://i.imgur.com/%s%s"%(self.hash, self.ext)
        self.thumbnail_url = "http://i.imgur.com/%sb%s"%(self.hash, self.ext)

    def cache_locally(self):
        "Fires the asynchronous task that will make a local copy of the image"
        download_image.delay(self)
