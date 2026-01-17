from django import forms
from .models import BookItem, Author, Publisher, Review

class BookItemForm(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ["Titel", "Author", "Veröffentlichungsdatum", "Genre", "Beschreibung"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["Vorname", "Nachname", "Geburtsdatum", "Biografie"]

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["Name", "Gründungsjahr", "Sitz", "Beschreibung"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["Buch", "Rezensent", "Bewertung", "Kommentar", "Datum"]