from django.shortcuts import render, redirect
from movies.models import Movies
from django.contrib import messages
import requests


imdb_url = 'http://www.omdbapi.com/?i={}&apikey=5badf7bf'


# Create your views here.
def home_page(request):
    #for mov in Movies.objects.all():
    #   res = requests.get(imdb_url.format(mov))
    #  res += res
    user_query = str(request.GET.get('query', ''))
    result_set = Movies.objects.filter(Name__icontains=user_query)

    context = {'result_set': result_set}
    return render(request, 'movies/home_page.html', context)


# Create a new movie
def create(request):
    if request.method == 'POST':
        mov_obj = Movies(Name=request.POST.get('name'), Picture=request.POST.get('url'),
                         Rating=request.POST.get('rating'), Notes=request.POST.get('notes'))
        try:
            mov_obj.save()
            messages.success(request, 'New movie: {} has been added successfully!'.format(request.POST.get('name')))
        except Exception as e:
            messages.warning(request, 'Got an error when trying to create new movie: {}'.format(e))
    return redirect('/')


def edit(request, movie_id):
    if request.method == 'POST':
        # edit_mov_obj = Movies.objects.get(id=movie_id)
        # edit_mov_obj.Name = request.POST.get('name')
        # edit_mov_obj.Picture = request.POST.get('url')
        # edit_mov_obj.Rating = request.POST.get('rating')
        # edit_mov_obj.Notes = request.POST.get('notes')
        # edit_mov_obj.save()
        try:
            Movies.objects.filter(id=movie_id).update(Name=request.POST.get('name'), Picture=request.POST.get('url'), Rating=request.POST.get('rating'), Notes=request.POST.get('notes'))
            messages.success(request, '{} has been updated successfully!'. format(request.POST.get('name')))
        except Exception as e:
            messages.warning(request, 'Got an error {} when trying to update {} movie'.format(e, request.POST.get('name')))
    return redirect('/')


def delete(request, movie_id):

    try:
        del_mov_obj = Movies.objects.get(id=movie_id)
        movie_name = Movies.objects.get(id=movie_id)
        del_mov_obj.delete()
        messages.success(request, '{} has been deleted successfully!'.format(movie_name.Name))
    except Exception as e:
        messages.warning(request, 'Got an error {} when trying to delete a movie'.format(e, request.POST.get('name')))
    return redirect('/')

