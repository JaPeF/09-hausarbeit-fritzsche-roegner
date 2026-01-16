from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import BookItem
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from .forms import BookItemForm

# Create your views here.

def home(request):
    return render(request, "library/home.html")

class BookListView(ListView):
    model = BookItem
    template_name = "library/book/book_list.html"
    context_object_name = "all_items"

class BookDetailView(DetailView):
    model = BookItem
    template_name = "library/book/book_detail.html"
    context_object_name = "book"

class BookCreateView(CreateView):
    model = BookItem
    form_class = BookItemForm
    template_name = "library/book/book_form.html"
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    model = BookItem
    form_class = BookItemForm
    template_name = "library/book/book_form.html"
    success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView):
    model = BookItem
    template_name = "library/book/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")


def author_list(request):
    return render(request, "library/author/author_list.html")

def publisher_list(request):
    return render(request, "library/publisher/publisher.html")

def review_list(request):
    return render(request, "library/reviews/review.html")
