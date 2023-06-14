from django.shortcuts import render

pokemon = [
    {'name': 'Bulbasaur', 'number': 1, 'weight': '6.9kg', 'height': '0.7m', 'type': 'Grass/Poison'},
    {'name': 'Charmander', 'number': 4, 'weight': '8.5kg', 'height': '0.6m', 'type': 'Fire'},
    {'name': 'Squirtle', 'number': 7, 'weight': '9.0kg', 'height': '0.5m', 'type': 'Water'},
    {'name': 'Pikachu', 'number': 25, 'weight': '6.0kg', 'height': '0.4m', 'type': 'Electric'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def allpokemon_index(request):
    return render(request, 'allpokemon/index.html', {
        'allpokemon': pokemon
    })