from celery import task
from settings import PROJECT_ROOT

import urllib
import time, os

@task
def download_image(image):
    """Downloads the image asynchronously and saves it into the 'images' folder"""
    r = urllib.urlopen(image.url)
    images = os.path.join(PROJECT_ROOT, 'images')

    f = file("%s/%s%s"%(images, image.hash, image.ext), 'w')
    f.write(r.read())
    f.close()

    return True
