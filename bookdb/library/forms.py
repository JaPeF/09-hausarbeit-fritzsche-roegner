from django import forms
from .models import BookItem

class BookItemForm(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = ["Titel", "Veröffentlichungsdatum", "Genre", "Beschreibung"]
