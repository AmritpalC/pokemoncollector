from django.shortcuts import render, redirect

#Importing CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Importing Pokemon model and FeedingForm
from .models import Pokemon, Item
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/index.html', {
        'pokemons': pokemons
    })

def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    id_list = pokemon.items.all().values_list('id')
    items_pokemon_doesnt_have = Item.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'pokemons/detail.html', {
        'pokemon': pokemon, 'feeding_form': feeding_form,
        'items': items_pokemon_doesnt_have
    })

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'number', 'weight', 'height', 'type', 'description']

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['weight', 'height', 'description']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons'

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('detail', pokemon_id=pokemon_id)

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items'

def assoc_item(request, pokemon_id, item_id):
   Pokemon.objects.get(id=pokemon_id).items.add(item_id)
   return redirect('detail', pokemon_id=pokemon_id)

def unassoc_item(request, pokemon_id, item_id):
   Pokemon.objects.get(id=pokemon_id).items.remove(item_id)
   return redirect('detail', pokemon_id=pokemon_id)
