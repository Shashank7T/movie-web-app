from django.shortcuts import render
from movies.models import Movies

# Create your views here.
def home_page(request):
    result_set = Movies.objects.all()
    context = {'result_set': result_set}
    return render(request, 'movies/home_page.html', context)
