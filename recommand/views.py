from django.shortcuts import render
from .models import Movie

# Create your views here.

def home(request):
    return render(request, 'recommand/home.html', {})

def ost_search(request):
    return render(request, 'recommand/ost_search.html', {})

def movielist(request):
    return render(request, 'recommand/repage.html', {})

# def movielist(request):
#     movies = Movie.objects.filter(name__contains=movies).order_by("movie_id")
#     return render(request, "recommand/movielist.html", {
#         "movie_list":movies,
#     })
#
#
# def search(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         movies = Movie.objects.filter(name__contains=searched)
#         return render(request, 'recommand/recommand.html', {
#             'searched':searched, 'movies':movies
#         })
#     else:
#         return render(request, 'recommand/recommand.html', {})
