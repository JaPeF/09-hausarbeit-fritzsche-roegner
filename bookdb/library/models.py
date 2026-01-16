from django.db import models
from datetime import date

# Create your models here.
class BookItem(models.Model):
    Titel = models.CharField(max_length=200)
    Veröffentlichungsdatum = models.DateField(default=date.today)
    Genre = models.CharField(max_length=100, blank=True)
    Beschreibung = models.TextField(blank=True)

    def __str__(self):
        return self.Titel