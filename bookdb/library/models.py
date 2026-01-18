from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Author(models.Model):
    Vorname = models.CharField(max_length=100)
    Nachname = models.CharField(max_length=100)
    Geburtsdatum = models.DateField(null=True, blank=True)
    Biografie = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Vorname} {self.Nachname}"
    
class Publisher(models.Model):
    Name = models.CharField(max_length=200)
    Gründungsjahr = models.PositiveIntegerField(null=True, blank=True)
    Sitz = models.CharField(max_length=200, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.Name

class BookItem(models.Model):
    Titel = models.CharField(max_length=200)
    Author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    Veröffentlichungsdatum = models.DateField(default=date.today)
    Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    Genre = models.CharField(max_length=100, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.Titel
    
class Review(models.Model):
    Buch = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name="reviews")
    Rezensent = models.CharField(max_length=100)
    Bewertung = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    Kommentar = models.TextField(blank=True)
    Datum = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.Buch} - {self.Bewertung}/10"
    
class FavoriteEntry(models.Model):
    Buch = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name="favorite_entries")
    AngelegtAm = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["Buch"], name="unique_favorite_book")
        ]

    def __str__(self):
        return f"Favorit: {self.Buch}"