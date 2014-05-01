from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse

from pokemon.models import Pokemon 

# Create your views here.

def index(request):
	return HttpResponse("THIS IS NOT COMPLETE YET")