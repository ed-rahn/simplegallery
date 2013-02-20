from celery import task
import requests

@task
def download_image(image):
    """Downloads the image asynchronously and saves it into the 'images' folder"""
    print "Exercise left to the reader!"
