from django.db import models

# Create your models here.
class Author(models.Model):
    """Author for one of the images"""
    added = models.DateTimeField(auto_now_add=True, auto_now=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('authors-detail', [self.pk])

