from django.views.generic import ListView, DetailView
from models import Author

class AuthorListView(ListView):
    template_name = "authors/list.html"
    model = Author

class AuthorDetailView(DetailView):
    template_name = "authors/detail.html"
    model = Author
