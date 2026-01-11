from django.db import models
from datetime import date

# Create your models here.
class BookItem(models.Model):
    Titel = models.CharField()
    Veröffentlichungsdatum = models.DateField(default=date.today)
    Genre = models.CharField()
    Beschreibung = models.CharField()