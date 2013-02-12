from django.views.generic import ListView, DetailView
from models import Image

class GalleryView(ListView):
    template_name = "gallery/list.html"
    model = Image

class GalleryDetailView(DetailView):
    template_name = "gallery/detail.html"
    model = Image

class GalleryByAuthorView(ListView):
    pass
