from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

from pokemon.models import Pokemon 

# Create your views here.

def index(request):
	return HttpResponse("THIS IS NOT COMPLETE YET")

def pokemon_profile(request, pokemon_id):
	#template = loader.get_template('pokemon/pokemon_profile.html')
	context = {'test':'foobar'}
	return render(request, 'pokemon/pokemon_profile.html', context)