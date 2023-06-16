from django.db import models

from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    height = models.DecimalField(max_digits=7, decimal_places=1)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __stri__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})