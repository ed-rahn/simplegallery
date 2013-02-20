from datetime import datetime

from django.core.management.base import NoArgsCommand, CommandError
import requests
import simplejson

from authors.models import Author
from gallery.models import Image

IMGUR_GALLERY_URL='http://imgur.com/gallery.json'

class Command(NoArgsCommand):
    help = "Import images from Imgur gallery"

    def get_or_create_author(self, author_name):
        """
        For convenience, creates an author if one with this name doesn't exist.
        """
        # TODO: make sure that this method doesn't add repeated authors
        author, created = Author.objects.get_or_create(name=author_name)
        return author

    def parse_datetime(self, text):
        """
        Takes a string in the format %Y-%m-%d %H:%M:%S and returns the corresponding
        datetime.datetime object representing it
        """
        FORMAT = '%Y-%m-%d %H:%M:%S'
        return datetime.strptime(text, FORMAT)


    def process_image(self, image_data):
        """
        Takes the dictionary representing an image and saves it to an instance of
        the gallery.Image model.
        """
        author_name = image_data['account_url']
        if author_name:
            new = Image()
            new.title = image_data['title']
            new.size = image_data['size']
            new.hash = image_data['hash']
            new.ext = image_data['ext']

            # TODO: make sure all these methods are implemented correctly
            new.author = self.get_or_create_author(author_name)
            new.timestamp = self.parse_datetime(image_data['timestamp'])
            new.build_urls()
            new.save()
        else:
            print "Image %(hash)s didn't have an author" % image_data

    def handle_noargs(self, **options):
        response = requests.get(IMGUR_GALLERY_URL)

        # If we've got a successful response, parse the data
        if response.status_code == 200:
            json_data = simplejson.loads(response.text)

            # Save each image
            for image_data in json_data.get('data', []):
                self.process_image(image_data)
        else:
            # If the response is anything else, fail with CommandError
            raise CommandError("Error response when reading from Imgur")
