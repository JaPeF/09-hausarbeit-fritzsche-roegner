from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import BookItem, Author, Publisher, Review
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from .forms import BookItemForm, AuthorForm, PublisherForm, ReviewForm
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import BookItem, FavoriteEntry

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
        search_query = self.request.GET.get("q")
        
        if search_query:
            keywords = search_query.split()
            q_objects = Q()
            
            for word in keywords:
                q_objects |= Q(Titel__icontains=word)
                q_objects |= Q(Author__Vorname__icontains=word)
                q_objects |= Q(Author__Nachname__icontains=word)
                q_objects |= Q(Genre__icontains=word)
            
            queryset = queryset.filter(q_objects).distinct()
            
        return queryset

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
# -------------
# Favoritenliste

def favorites_list(request):
    favorites = FavoriteEntry.objects.select_related("Buch").order_by("-AngelegtAm")
    return render(request, "library/favoriten/favorites_list.html", {"favorites": favorites})


def favorites_add(request):
    # Alle Bücher anzeigen, aber nur die, die noch nicht Favorit sind
    favorite_book_ids = FavoriteEntry.objects.values_list("Buch_id", flat=True)
    books = BookItem.objects.exclude(pk__in=favorite_book_ids).order_by("Titel")

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        if book_id:
            book = get_object_or_404(BookItem, pk=book_id)
            FavoriteEntry.objects.get_or_create(Buch=book)
            return redirect("favorites_list")

    return render(request, "library/favoriten/favorites_add.html", {"books": books})


def favorites_remove(request, pk):
    # pk ist Buch-ID
    FavoriteEntry.objects.filter(Buch_id=pk).delete()
    return redirect(request.META.get("HTTP_REFERER", "favorites_list"))


def favorites_toggle(request, pk):
    # pk ist Buch-ID
    book = get_object_or_404(BookItem, pk=pk)
    fav = FavoriteEntry.objects.filter(Buch=book).first()
    if fav:
        fav.delete()
    else:
        FavoriteEntry.objects.create(Buch=book)

    return redirect(request.META.get("HTTP_REFERER", "favorites_list"))