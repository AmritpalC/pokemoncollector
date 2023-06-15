from django.contrib import admin

#importing model
from .models import Pokemon

# Register your models here.
admin.site.register(Pokemon)