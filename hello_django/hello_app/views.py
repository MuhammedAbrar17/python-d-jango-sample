from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def printHello(request):
    movie_data={'movies':[{
        'title' : 'vellimoonga',
        'year'  : 2002,
        'summary' : 'story of foolish politics',
        'sucess' : True, 
    },
      {
        'title' : 'Godfather',
        'year'  : 2001,
        'sucess' : False, 
    },
      {
        'title' : 'shikkarishambo',
        'year'  : 2010,
        'summary' : 'story of huntting',
        'sucess' : True, 
    },
      {
        'title' : 'LEO',
        'year'  : 2023,
        'summary' : 'story of one danger person',
        'sucess' : True, 
    },
      {
        'title' : 'kaithi',
        'year'  : 2021,
        'summary' : 'story of on night',
        'sucess' : True, 
    },]}
    return render(request,'hello.html',movie_data) 
