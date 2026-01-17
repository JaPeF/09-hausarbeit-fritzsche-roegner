from django import forms
from .models import BookItem, Author, Publisher, Review

class BookItemForm(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ["Titel", "Author", "Veröffentlichungsdatum", "Genre", "Publisher", "Beschreibung"]
        widgets = {
            'Author': forms.Select(),
            'Publisher': forms.Select(),
            'Veröffentlichungsdatum': forms.DateInput(attrs={'type': 'date'}),
            'Genre': forms.TextInput(),
            'Beschreibung': forms.Textarea(attrs={'rows': 4}),
        }

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