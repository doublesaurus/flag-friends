from django.db import models

# Create your models here.
class Country(models.Model):
    symbol = models.CharField(max_length=64)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"



