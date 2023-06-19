from django.db import models
from django.urls import reverse
from datetime import date

# Tuple of 2-tuples
BERRIES = (
    ('R', 'Razz'),
    ('N', 'Nanab'),
    ('P', 'Pinap'),
)


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    height = models.DecimalField(max_digits=7, decimal_places=1)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(BERRIES)
    

# New model - Feeding berries
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    berry = models.CharField(
        max_length=1, 
        choices=BERRIES,
        default=BERRIES[0][0]
    )

    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_berry_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
