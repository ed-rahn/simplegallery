from django.views.generic import ListView, DetailView
from models import Image

class GalleryView(ListView):
    template_name = "gallery/list.html"
    model = Image

    def get_queryset(self):
        title = self.request.GET.get('query', None)

        if title:
            return Image.objects.filter(title__contains=title)
        else:
            return Image.objects.all()

class GalleryDetailView(DetailView):
    template_name = "gallery/detail.html"
    model = Image

class GalleryByAuthorView(ListView):
    template_name = "gallery/list.html"

    def get_queryset(self):
        return Image.objects.filter(author=self.kwargs['authorname'])
