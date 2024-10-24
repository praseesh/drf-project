from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(movie)
    data = {
        'name' : movie.name,
        'description': movie.description,
        'active': movie.active
     }
    return JsonResponse(data)
