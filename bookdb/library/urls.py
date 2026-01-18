from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),
    # Falscher Link
    path("", views.home, name="home"),
    # Books
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    # Authors
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/new/", views.AuthorCreateView.as_view(), name="author_create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("authors/<int:pk>/edit/", views.AuthorUpdateView.as_view(), name="author_update"),
    path("authors/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author_delete"),
    # Publishers
    path("publishers/", views.PublisherListView.as_view(), name="publisher_list"),
    path("publishers/new/", views.PublisherCreateView.as_view(), name="publisher_create"),
    path("publishers/<int:pk>/", views.PublisherDetailView.as_view(), name="publisher_detail"),
    path("publishers/<int:pk>/edit/", views.PublisherUpdateView.as_view(), name="publisher_update"),
    path("publishers/<int:pk>/delete/", views.PublisherDeleteView.as_view(), name="publisher_delete"),
    # Reviews
    path("reviews/", views.ReviewListView.as_view(), name="review_list"),
    path("reviews/new/", views.ReviewCreateView.as_view(), name="review_create"),
    path("reviews/<int:pk>/", views.ReviewDetailView.as_view(), name="review_detail"),
    path("reviews/<int:pk>/edit/", views.ReviewUpdateView.as_view(), name="review_update"),
    path("reviews/<int:pk>/delete/", views.ReviewDeleteView.as_view(), name="review_delete"),
]
