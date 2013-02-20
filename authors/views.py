from django.views.generic import ListView, DetailView
from models import Author
from gallery.models import Image

class AuthorListView(ListView):
    template_name = "authors/list.html"
    model = Author


class AuthorDetailView(DetailView):
    template_name = "authors/detail.html"
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.filter(author=kwargs['object'].pk)
        return context
