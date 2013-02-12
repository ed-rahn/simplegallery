from django.db import models
from authors.models import Author

class Image(models.Model):
    """Gallery image, linked to an Author"""
    author = models.ForeignKey(Author, related_name='images')
    timestamp = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=250)
    hash = models.CharField(max_length=10)
    ext = models.CharField(max_length=4)
    size = models.PositiveIntegerField()
    url = models.URLField(verify_exists=False, max_length=200, blank=True)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('gallery-detail', [self.pk])

    def build_url(self):
        """
        Using the `hash` and `ext` members of the image, builds the URL of
        the image on the Imgur server.
        """
        # TODO: complete this by browsing around Imgur for a bit and checking
        # what the URL pattern looks like
        self.url = "i.imgur.com/%s%s"%(self.hash, self.ext)
