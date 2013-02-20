from django.views.generic import ListView, DetailView
from django.core.cache import cache
from django.http import Http404, HttpResponse
from models import Image
import json


class GalleryView(ListView):
    template_name = "gallery/list.html"
    model = Image

    def get_query(self):
        title = self.request.GET.get('query', None)

        if title:
            query = cache.get(title)
            if query is None:
                query = Image.objects.filter(title__contains=title)
                cache.set(title, query)
            return query 
        else:
            return None


    def get_queryset(self):
        query = self.get_query()
        if query is None:
            query = Image.objects.all()

        return query

    def get(self, *args, **kwargs):
        format = self.request.GET.get('format', None)
        query = self.get_query()

        if format == 'json' and query is None:
            raise Http404
        elif format == 'json' and query:
            json_list = []
            for image in query:
                json_list.append({'title': image.title,
                                'author': image.author.name,
                                'timestamp': str(image.timestamp),
                                'hash': image.hash,
                                'ext': image.ext,
                                'size': image.size,
                                'url': image.url})
                
            return HttpResponse(json.dumps(json_list))
        else:
            return super(GalleryView, self).get(*args, **kwargs)

class GalleryDetailView(DetailView):
    template_name = "gallery/detail.html"
    model = Image

class GalleryByAuthorView(ListView):
    template_name = "gallery/list.html"

    def get_queryset(self):
        return Image.objects.filter(author=self.kwargs['authorname'])
