from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    Vorname = models.CharField(max_length=100)
    Nachname = models.CharField(max_length=100)
    Geburtsdatum = models.DateField(null=True, blank=True)
    Biografie = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Publisher(models.Model):
    Name = models.CharField(max_length=200)
    Gründungsjahr = models.PositiveIntegerField(null=True, blank=True)
    Sitz = models.CharField(max_length=200, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BookItem(models.Model):
    Titel = models.CharField(max_length=200)
    Author = models.CharField(max_length=200, default="Unbekannt")
    Veröffentlichungsdatum = models.DateField(default=date.today)
    Genre = models.CharField(max_length=100, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.Titel
    
class Review(models.Model):
    Buch = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name="reviews")
    Rezensent = models.CharField(max_length=100)
    Bewertung = models.PositiveSmallIntegerField()
    Kommentar = models.TextField(blank=True)
    Datum = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.book} - {self.rating}/5"