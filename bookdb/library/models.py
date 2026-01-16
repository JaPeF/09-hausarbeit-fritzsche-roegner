from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BookItem(models.Model):
    Titel = models.CharField(max_length=200)
    Veröffentlichungsdatum = models.DateField(default=date.today)
    Genre = models.CharField(max_length=100, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.Titel
    
class Review(models.Model):
    book = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.CharField(max_length=100)  # Pseudonym
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.book} - {self.rating}/5"