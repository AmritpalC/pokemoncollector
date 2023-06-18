from django.db import models

from django.urls import reverse

# Tuple of 2-tuples
BERRIES = (
    ('R', 'Razz'),
    ('N', 'Nanab'),
    ('P', 'Pinap'),
)

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    height = models.DecimalField(max_digits=7, decimal_places=1)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})
    
# New model - berries
class Feeding(models.Model):
    date = models.DateField('feeding date')
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
