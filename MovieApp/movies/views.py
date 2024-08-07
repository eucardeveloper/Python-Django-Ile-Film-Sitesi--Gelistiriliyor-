from django.shortcuts import render
from .models import Category, Movie


def homePage(request):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html" , data)


def movies(request):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.all()
    }
    return render(request, "movies.html", data)

def movieDetails(request, id):
    data = {
        "movie" : Movie.objects.get(id=id)
    }
    return render(request, "moviedetails.html", data)