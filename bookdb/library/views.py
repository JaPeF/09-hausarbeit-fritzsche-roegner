from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import BookItem, Author, Publisher, Review
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from .forms import BookItemForm, AuthorForm, PublisherForm, ReviewForm
from django.db.models import Q, Avg

# Create your views here.

def home(request):
    return render(request, "library/home.html")
# -------------
# Book CRUD

class BookListView(ListView):
    model = BookItem
    template_name = "library/book/book_list.html"
    context_object_name = "all_items"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        q = self.request.GET.get("q")
        genre = self.request.GET.get("genre")
        publisher = self.request.GET.get("publisher")
        ratings = self.request.GET.get("rating")
        author = self.request.GET.get("author")
        
        if q:
            queryset = queryset.filter(
                Q(Titel__icontains=q) |
                Q(Author__Vorname__icontains=q) |
                Q(Author__Nachname__icontains=q) |
                Q(Genre__icontains=q)
            )
        
        if genre:
            queryset = queryset.filter(Genre=genre)
            
        if publisher:
            queryset = queryset.filter(Publisher_id=publisher)
        
        if ratings:
            queryset = queryset.filter(avg_rating__gte=min(ratings))
            
        if author:
            queryset = queryset.filter(Author_id=author)
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["genres"] = (BookItem.objects.values_list("Genre", flat=True).exclude(Genre="").distinct())
        context["publishers"] = Publisher.objects.all()
        context["authors"] = Author.objects.all()
        
        return context

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
    context_object_name = "author"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "library/author/author_detail.html"
    context_object_name = "author"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = BookItem.objects.filter(Author=self.object)
        return context

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
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(Name__icontains=search_query)
        return queryset

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "library/publisher/publisher_detail.html"
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
    template_name = "library/reviews/review_detail.html"
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
    
# -------------
# Suchleiste
def book_list(request):
    query = request.GET.get("q")
    print("QUERY:", query)
    books = BookItem.objects.all()
    
    if query:
        books = books.filter(Titel__icontains=query)
        
    return render(request, "library/book/book_list.html", {
                  "all_items": books,
                  "query": query,
                  })