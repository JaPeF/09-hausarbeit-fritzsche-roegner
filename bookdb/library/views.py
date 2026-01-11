from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import BookItem

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    if request.method == 'POST':
        print('Received data:', request.POST['itemName'])
        BookItem.objects.create(Titel = request.POST['itemName'])
    all_items = BookItem.objects.all()
    return render(request, "library/book/book_list.html", {'all_items': all_items})

def author_list(request):
    return render(request, "library/author/author_list.html")

def publisher_list(request):
    return render(request, "library/publisher/publisher.html")

def review_list(request):
    return render(request, "library/reviews/review.html")
