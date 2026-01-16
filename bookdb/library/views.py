from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import BookItem, Author, Publisher, Review
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from .forms import BookItemForm, AuthorForm, PublisherForm, ReviewForm

# Create your views here.

def home(request):
    return render(request, "library/home.html")
# -------------
# Book CRUD

class BookListView(ListView):
    model = BookItem
    template_name = "library/book/book_list.html"
    context_object_name = "all_items"

class BookDetailView(DetailView):
    model = BookItem
    template_name = "library/book/book_detail.html"

class BookCreateView(CreateView):
    model = BookItem
    form_class = BookItemForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    model = BookItem
    form_class = BookItemForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView):
    model = BookItem
    template_name = "library/generic_confirm_delete.html"
    success_url = reverse_lazy("book_list")
# -------------
# Author CRUD

class AuthorListView(ListView):
    model = Author
    template_name = "library/author/author_list.html"
    context_object_name = "authors"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "library/generic_detail.html"
    context_object_name = "author"

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("author_list")

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("author_list")

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "library/generic_confirm_delete.html"
    success_url = reverse_lazy("author_list")
# -------------
# Publisher CRUD

class PublisherListView(ListView):
    model = Publisher
    template_name = "library/publisher/publisher_list.html"
    context_object_name = "publishers"

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "library/generic_detail.html"
    context_object_name = "publisher"

class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("publisher_list")

class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("publisher_list")

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = "library/generic_confirm_delete.html"
    success_url = reverse_lazy("publisher_list")
# -------------
# Review CRUD

class ReviewListView(ListView):
    model = Review
    template_name = "library/reviews/review_list.html"
    context_object_name = "reviews"

class ReviewDetailView(DetailView):
    model = Review
    template_name = "library/generic_detail.html"
    context_object_name = "review"

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("review_list")

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "library/generic_forms.html"
    success_url = reverse_lazy("review_list")

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "library/generic_confirm_delete.html"
    success_url = reverse_lazy("review_list")